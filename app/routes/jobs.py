from fastapi import APIRouter
from ..services.jobs_service import JobService
from ..models.job import Job

router = APIRouter()

service = JobService()

@router.post('/jobs', response_model=Job, tags=['Plantões'])
async def createDoctor(job: Job):
    return service.create(job)

@router.get('/jobs', tags=['Plantões'])
async def listAllJobs():
    return service.get_all()

@router.get('/jobs/{crm}', tags=['Plantões'])
async def getDoctorByCRM(crm):
    return service.get_by_crm(crm)
