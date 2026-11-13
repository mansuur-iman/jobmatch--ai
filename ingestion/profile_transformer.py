def transform_profile(profile: dict) -> str:
    lines = []

    def add(label: str, value: str):
        if value:
            lines.append(f"{label}: {value}")

    add("Preferred Roles", ", ".join(profile.get("roles") or []))
    add("Job Level", profile.get("jobLevel") or "")
    add("Skills", ", ".join(profile.get("skills") or []))
    add("Certifications", ", ".join(profile.get("certifications") or []))
    add("Degree", profile.get("degree") or "")

    projects = profile.get("projects") or []
    if projects:
        lines.append("Projects:")
        lines += [
            f"- {p.get('name') or 'Unnamed project'}: {p.get('description') or ''}"
            for p in projects
        ]

    experience = profile.get("experience") or []
    if experience:
        lines.append("Experience:")
        lines += [
            f"- {e.get('title') or ''} at {e.get('company') or ''}: {e.get('description') or ''}"
            for e in experience
        ]

    return "\n".join(lines)


def profile_filters(profile: dict) -> dict:
    """Hard constraints for metadata filtering, not embedded."""
    return {
        "workEnvironment": profile.get("workEnvironment"),
        "workLocation": profile.get("workLocation"),
        "languages": profile.get("languages") or [],
        "availability": profile.get("availability"),
    }