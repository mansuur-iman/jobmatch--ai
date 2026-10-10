def transform_profile(profile: dict) -> str:
    projects = profile.get("projects") or []

    project_text = "\n".join(
        f"- {project.get('name', 'Unnamed project')}: "
        f"{project.get('description', '')}"
        for project in projects
    )

    content = (
        f"University: {profile.get('university', 'Not specified')}\n"
        f"Degree: {profile.get('degree', 'Not specified')}\n"
        f"Skills: {', '.join(profile.get('skills') or [])}\n"
        f"Work Environment: {profile.get('workEnvironment', 'Not specified')}\n"
        f"Work Location: {profile.get('workLocation', 'Not specified')}\n"
        f"Certifications: {', '.join(profile.get('certifications') or [])}\n"
        f"Projects:\n{project_text}\n"
        f"Languages: {', '.join(profile.get('languages') or [])}\n"
        f"Job Level: {profile.get('jobLevel', 'Not specified')}\n"
        f"Availability: {profile.get('availability', 'Not specified')}\n"
        f"Preferred Roles: {', '.join(profile.get('roles') or [])}"
    )

    return content