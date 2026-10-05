
from langchain_core.documents import Document
def transform_job(job:dict)-> Document:
  try:
    content = (
      f"Title: {job['title']}\n"
      f"Location: {job['location']}\n"
      f"Description: {job['description']}\n"
      f"Required Skills: {(', ').join(job['requiredSkills'])}\n"
      f"Employment Type: {job['employmentType']}\n"
      f"Company: {job['company']}\n"
    )

    metadata = {
        "job_id": job["id"]
    }

    return Document(
      page_content=content,
      metadata=metadata
    )
  except Exception as e:
    print(f"Error in processing jobs: {e}")
