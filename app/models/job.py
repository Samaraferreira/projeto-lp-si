from pydantic import BaseModel
from datetime import datetime
from ..enums import DepartmentEnum, StatusEnum

class Job(BaseModel):
    id:str
    doctor_crm:str
    department: DepartmentEnum = DepartmentEnum.DEFAULT
    period:str
    date: datetime
    status: StatusEnum = StatusEnum.AGENDADO