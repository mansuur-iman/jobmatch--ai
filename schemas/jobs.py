from pydantic import BaseModel
class Jobin(BaseModel):
   id:str
   title:str
   description:str
   employmentType:str
   requiredSkills:list[str]
   company:str
   location:str

class IndexRequest(BaseModel):
   jobs:list[Jobin]
