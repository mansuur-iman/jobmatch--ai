from pydantic import BaseModel, Field

class MatchRequest(BaseModel):
   profile:dict
   job:str

class JobMatchOutPut(BaseModel):
   matching_requirements: list[str] = Field(decription="List of candidate fields that matched the job description")
   missing_requirements : list[str] = Field(description="List of requirements expilicitly mentioned in the jobbut are missing from the candidate profile.")
   important_gaps : list[str] = Field(description="Critical architectural or domain gaps that represent a high risk for the role.")
   overall_match_explanation : str = Field(description="A comprehensive technical summary explaining the final matching verdict.")
   match_score : int = Field(description="A matching percentage score from 0 to 100 based strictly on requirements met.")

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
