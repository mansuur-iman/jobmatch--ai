from ingestion.profile_transformer import transform_profile, profile_filters


def make_profile(**overrides):
    profile = {
        "skills": ["Python", "FastAPI"],
        "roles": ["Backend Developer", "API Developer"],
        "jobLevel": "Senior",
        "certifications": ["AWS Certified Developer"],
        "degree": "Bachelor's in Computer Science",
        "university": "University of Nairobi",
        "projects": [
            {"name": "Project A", "description": "A project about A"},
            {"name": "Project B", "description": "A project about B"},
        ],
        "experience": [
            {"title": "Intern", "company": "Acme", "description": "Built APIs"},
        ],
        "workEnvironment": "Remote",
        "workLocation": None,
        "languages": ["English", "Swahili"],
        "availability": "Immediate",
    }
    return profile | overrides


def test_embedding_text_includes_semantic_fields():
    result = transform_profile(make_profile())

    assert "Preferred Roles: Backend Developer, API Developer" in result
    assert "Job Level: Senior" in result
    assert "Skills: Python, FastAPI" in result
    assert "Certifications: AWS Certified Developer" in result
    assert "Degree: Bachelor's in Computer Science" in result
    assert "- Project A: A project about A" in result
    assert "- Project B: A project about B" in result
    assert "- Intern at Acme: Built APIs" in result


def test_embedding_text_excludes_non_semantic_fields():
    result = transform_profile(make_profile(workLocation="Nairobi"))

    assert "University" not in result
    assert "Availability" not in result
    assert "Languages" not in result
    assert "Work Environment" not in result
    assert "Work Location" not in result


def test_empty_fields_are_omitted_not_filled():
    result = transform_profile(
        make_profile(certifications=[], degree=None, experience=None)
    )

    assert "Certifications" not in result
    assert "Degree" not in result
    assert "Experience" not in result
    assert "None" not in result
    assert "Not specified" not in result


def test_empty_profile_does_not_crash():
    assert transform_profile({}) == ""


def test_profile_filters_returns_hard_constraints():
    filters = profile_filters(make_profile())

    assert filters == {
        "workEnvironment": "Remote",
        "workLocation": None,
        "languages": ["English", "Swahili"],
        "availability": "Immediate",
    }


def test_profile_filters_handles_missing_keys():
    filters = profile_filters({})

    assert filters["languages"] == []
    assert filters["workEnvironment"] is None