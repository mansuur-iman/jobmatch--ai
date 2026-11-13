
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def job_payload(job_id):
     return {
        "id": job_id,
        "title": "Dev",
        "company": "Acme",
        "employmentType": "FULL_TIME",
        "description": "x",
        "requiredSkills": ["Python"],
        "location": "Nairobi",
    }

def test_index_reports_partial_failure():
    def fake_ingest(job):
        if job["id"] == "bad":
            raise RuntimeError("boom")
        return 3

    with patch("routes.indexer.ingest_job", side_effect=fake_ingest):
        r = client.post("api/v1/jobs/index", json={"jobs": [job_payload("a"), job_payload("bad")]})


    assert r.status_code == 200
    assert r.json() == {"indexed": ["a"], "failed": ["bad"]}

def test_index_rejects_bad_payload():
    assert client.post("api/v1/jobs/index", json={}).status_code == 422