from fastapi import APIRouter
from ..services.doctor_service import service
from ..models.doctor import Doctor

router = APIRouter()

@router.post('/doctors', response_model=Doctor, tags=['Médicos'])
async def create_doctor(doctor: Doctor):
    return service.create(doctor)

@router.get('/doctors', response_model=list[Doctor], tags=['Médicos'])
async def list_all_doctors():
    return service.get_all()

@router.get('/doctors/search', response_model=list[Doctor], tags=['Médicos'])
async def search_doctors_by_name(name: str):
    return service.get_by_name(name)

@router.get('/doctors/{crm}/unlock', tags=['Médicos'])
async def unlock_doctor(crm: str):
    return service.unlock_doctor(crm)

@router.get('/doctors/{crm}/lock', tags=['Médicos'])
async def lock_doctor(crm: str):
    return service.lock_doctor(crm)

@router.get('/doctors/{crm}', response_model=Doctor, tags=['Médicos'])
async def get_doctor_by_CRM(crm: str):
    return service.get_by_crm(crm)