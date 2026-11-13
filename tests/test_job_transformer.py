from ingestion.transformer import transform_job

def make_job(**overrides):
    job = {
        "id": "j1", "title": "Backend Engineer", "company": "Acme",
        "employmentType": "FULL_TIME", "description": "Build APIs",
        "requiredSkills": ["Python", "FastAPI"], "location": None,
    }
    return job | overrides

def test_transform_job_returns_document_with_expected_content_and_metadata():
    job = make_job()
    document = transform_job(job)

    assert "Title: Backend Engineer" in document.page_content
    assert "Required Skills: Python, FastAPI" in document.page_content
    assert document.metadata == {"job_id": "j1", "title": "Backend Engineer", "company": "Acme"}

def test_missing_location_defaults():
    assert "Location: Not specified" in transform_job(make_job()).page_content

def test_missing_skills_does_not_crash():
    transform_job(make_job(requiredSkills=None))