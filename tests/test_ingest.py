
from unittest.mock import Mock
from ingestion import ingest
from tests.test_job_transformer import make_job

def test_ingest_chunks_and_stores(monkeypatch):
    fake_store = Mock()
    monkeypatch.setattr(ingest, "get_vector_store_cached", lambda: fake_store)

    n = ingest.ingest_job(make_job(description="word " * 500))

    assert n > 1
    fake_store.add_documents.assert_called_once()
    ids = fake_store.add_documents.call_args.kwargs["ids"]
    assert len(ids) == n
    assert ids[0] == "j1:0"