from datetime import date
from fastapi import APIRouter
from ..services.jobs_service import service
from ..models.job import Job

router = APIRouter()

@router.post('/jobs', response_model=Job, tags=['Plantões'])
async def create_job(job: Job):
    return service.create(job)

@router.get('/jobs', tags=['Plantões'])
async def list_all_jobs():
    return service.get_all()

@router.get('/jobs/change', tags=['Plantões'])
async def change_doctor(crm: str, date: date, other_crm: str):
    return service.change_doctor(crm, date, other_crm)

@router.get('/jobs/filter', tags=['Plantões'])
async def filter_jobs(status: str, date: date, department: str, period: str):
    return service.filter_jobs(status, date, department, period)

@router.get('/jobs/{crm}', tags=['Plantões'])
async def get_jobs_by_doctor_CRM(crm: str):
    return service.get_by_crm(crm)