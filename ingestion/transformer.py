
from langchain_core.documents import Document
def transform_job(job:dict)-> Document:
  
    content = (
      f"Title: {job['title']}\n"
      f"Company: {job['company']}\n"
      f"Location: {job.get('location') or 'Not specified'}\n"
      f"Required Skills: {(', ').join(job.get('requiredSkills') or [])}\n"
      f"Employment Type: {job['employmentType']}\n"
      f"Description: {job['description']}\n"
    )

    metadata = {
        "job_id": job["id"],
        "title": job["title"],
        "company": job["company"]
    }

    return Document(
      page_content=content,
      metadata=metadata
    )

