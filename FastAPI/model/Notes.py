from pydantic import BaseModel, Field,EmailStr,field_validator
from bson import ObjectId
import datetime

class Notes(BaseModel):
    
    title:str=Field(...,example="Title of the note",min_length=3)
    notes:str=Field(...,example="Content of the note",min_length=3)
    dateofadd:datetime.datetime=Field(default_factory=datetime.datetime.now,example="2024-12-31T12:34:56")

    
    