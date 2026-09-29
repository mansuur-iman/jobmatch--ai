def transform_documents(candidate:dict)-> list:
    try:
        documents = []

        documents.append({
        "content": f"Skills: {', '.join(candidate['skills'])}",
        "source": "skills"
    })

        documents.append({
        "content": (
            f"University: {candidate['university']}\n"
            f"Education: {candidate['education']}"
        ),
        "source": "education"
    })

        documents.append({
        "content": f"Certifications: {', '.join(candidate['certifications'])}",
        "source": "certifications"
    })

        for project in candidate["projects"]:
         documents.append({
            "content": (
                f"Project: {project['name']}\n"
                f"Description: {project['description']}\n"
                f"Technologies: {', '.join(project['technologies'])}"
            ),
            "source": "projects"
        })

        documents.append({
        "content": f"Experience: {', '.join(candidate['experience'])}",
        "source": "experience"
    })

        documents.append({
        "content": f"Roles: {', '.join(candidate['prefered_roles'])}",
        "source": "roles"
    })

        documents.append({
        "content": f"Languages: {', '.join(candidate['languages'])}",
        "source": "languages"
    })

        return documents
    except Exception as e:
        print(f"Error occured while transforming data.. {e}")
