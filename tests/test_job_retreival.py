from unittest.mock import Mock, patch

from fastapi.testclient import TestClient
from langchain_core.documents import Document

from main import app

client = TestClient(app)


def hit(job_id, distance):
    return (Document(page_content="x", metadata={"job_id": job_id}), distance)


def post(store, **overrides):
    body = {"profile": {"skills": ["Python"]}, "excludeJobIds": []} | overrides
    with patch("routes.recommendation._store", return_value=store):
        return client.post("/api/v1/recommendation", json=body)


def fake_store(*hits):
    store = Mock()
    store.similarity_search_with_score.return_value = list(hits)
    return store


def test_duplicate_chunks_collapse_to_one_job():
    store = fake_store(hit("a", 0.1), hit("a", 0.2), hit("b", 0.3))
    r = post(store)

    assert r.status_code == 200
    ids = [x["job_id"] for x in r.json()["recommendations"]]
    assert ids == ["a", "b"]


def test_excluded_jobs_are_skipped():
    store = fake_store(hit("a", 0.1), hit("b", 0.2))
    r = post(store, excludeJobIds=["a"])

    ids = [x["job_id"] for x in r.json()["recommendations"]]
    assert ids == ["b"]


def test_results_capped_at_ten():
    store = fake_store(*[hit(f"j{i}", i / 100) for i in range(30)])
    r = post(store)

    assert len(r.json()["recommendations"]) == 10


def test_empty_profile_returns_422():
    r = post(fake_store(), profile={})
    assert r.status_code == 422


def test_vector_store_failure_returns_502():
    store = Mock()
    store.similarity_search_with_score.side_effect = RuntimeError("db down")
    r = post(store)

    assert r.status_code == 502