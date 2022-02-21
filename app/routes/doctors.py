from fastapi import APIRouter
from ..services.doctor_service import DoctorService
from ..models.doctor import Doctor

router = APIRouter()

service = DoctorService()

@router.post('/doctors', response_model=Doctor, tags=['Médicos'])
async def createDoctor(doctor: Doctor):
    return service.create(doctor)

@router.get('/doctors', tags=['Médicos'])
async def listAllDoctors():
    return service.get_all()

@router.get('/doctors/{crm}', tags=['Médicos'])
async def getDoctorByCRM(crm):
    return service.get_by_crm(crm)

@router.get('/doctors/search', tags=['Médicos'])
async def searchDoctorsByName(name):
    return service.get_by_name(name)