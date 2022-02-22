from datetime import date
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from .doctor_service import service as doctorService
from ..enums import DepartmentEnum, StatusEnum, PeriodEnum
from ..models.job import Job
import json

class JobService:
    def __init__(self):
        self.jobs = self.__getData()

    def create(self, job: Job):
        doctor = doctorService.get_by_crm(job.doctor_crm)
        if self.__checkIfThereIsAlreadyJobScheduledOnTheDate(job.doctor_crm, job.date):
            raise HTTPException(status_code=400, detail="Job can not be scheduled")
        else:
            if doctor.isActive:
                self.jobs.append(job)
                self.__saveData()
                return job
            else:
                raise HTTPException(status_code=400, detail="Job can not be scheduled")
        
    def get_all(self):
        return self.jobs

    def get_by_crm(self, crm):
        results = []
        for job in self.jobs:
            if job.doctor_crm == crm:
                results.append(job)
        if len(results) == 0:
            raise HTTPException(status_code=404, detail="job not found")
        else: return results

    def filter_jobs(self, status, date, department, period):
        results = []
        for job in self.jobs:
            if job.status.value == status and job.date == date and job.department.value == department and job.period.value == period:
                results.append(job)
        if len(results) == 0:
            raise HTTPException(status_code=404, detail="job not found")
        else: return results
    
    def get_job_by_crm_and_date(self, crm, date) -> Job:
        result = None
        for job in self.jobs:
            if job.date == date and job.doctor_crm == crm:
                result = job
        if not result:
            raise HTTPException(status_code=404, detail="job not found")
        else: return result

    def change_doctor(self, crm, date: date, other_crm):
        doctorService.get_by_crm(crm)
        doctorService.get_by_crm(other_crm)
        if self.__checkIfThereIsAlreadyJobScheduledOnTheDate(other_crm, date):
            raise HTTPException(status_code=400, detail="doctor already has a job scheduled")
        else:
            job = self.get_job_by_crm_and_date(crm, date)
            job.doctor_crm = other_crm
            return job

    def __checkIfThereIsAlreadyJobScheduledOnTheDate(self, doctor_crm, date):
        if len(self.jobs) > 0: 
            for job in self.jobs:
                if job.date == date and job.doctor_crm == doctor_crm:
                    return True
        else:
            return False
    
    def __saveData(self):
        with open('app/data/jobs.json', 'w') as json_file:
            json.dump(jsonable_encoder(self.jobs), json_file)

    def __getData(self) -> list: 
        with open('app/data/jobs.json') as json_file:
            data_dict = json.load(json_file)
            return self.__parseToJob(data_dict)

    def __parseToJob(self, data_dict: dict):
        list = []
        for data in data_dict:
            job = Job(id=data.get('id'),doctor_crm=data.get('doctor_crm'),department=data.get('department'),
                            period=data.get('period'),status=data.get('status'),date=data.get('date'))
            list.append(job)
        return list

service = JobService()  # Singleton