from pydantic import BaseModel
from datetime import date
from ..enums import DepartmentEnum, StatusEnum, PeriodEnum

class Job(BaseModel):
    id:str
    doctor_crm:str
    department: DepartmentEnum = DepartmentEnum.DEFAULT
    period: PeriodEnum = PeriodEnum.DEFAULT
    date: date
    status: StatusEnum = StatusEnum.AGENDADO