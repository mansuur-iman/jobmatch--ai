def transform_documents(profile:dict)-> list:
    try:
        documents = []

        user_id = profile["userId"]

        documents.append({
        "user_id": user_id,
        "content": f"Skills: {', '.join(profile['skills'])}",
        "source": "skills"
    })

        documents.append({
        "user_id":user_id,
        "content": (
            f"University: {profile['university']}\n"
            f"Degree: {profile['degree']}"
        ),
        "source": "education"
    })

        documents.append({
        "user_id": user_id,
        "content": f"Certifications: {', '.join(profile['certifications'])}",
        "source": "certifications"
    })

        for project in profile["projects"]:
         documents.append({
            "user_id": user_id,
            "content": (
                f"Project: {project['name']}\n"
                f"Description: {project['description']}\n"
                f"Technologies: {', '.join(project['technologies'])}"
            ),
            "source": "projects"
        })

        if profile.get("experience"):
         documents.append({
        "user_id": user_id,
        "content": f"Experience: {', '.join(profile['experience'])}",
        "source": "experience"
    })

        documents.append({
        "user_id":user_id,
        "content": f"Roles: {', '.join(profile['roles'])}",
        "source": "roles"
    })

        documents.append({
        "user_id": user_id,
        "content": f"Languages: {', '.join(profile['languages'])}",
        "source": "languages"
    })

        documents.append({
        "user_id": user_id,
        "content": (
          f"prefered work environment: {profile['workEnvironment']}\n",
          f"prefered work location: {profile['workLocation']}\n",
          f"job level: {profile['jobLevel']}\n",
          f"job availability: {profile['availability']}"
       ),
        "source": "preferences"
    })

        return documents
    except Exception as e:
        print(f"Error occured while transforming data.. {e}")
