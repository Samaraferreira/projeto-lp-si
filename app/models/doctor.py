from pydantic import BaseModel

class Doctor(BaseModel):
    crm:str
    name:str
    email:str
    specialty:str
    phone:str
    cpf:str
    isActive: bool = True