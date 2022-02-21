from fastapi import HTTPException
from .doctor_service import DoctorService
from ..models import job as Job

class JobService:
    def __init__(self):
        self.jobs = []
        self.doctorService = DoctorService()

    def create(self, job: Job):
        print(job.doctor_crm)
        doctor = self.doctorService.get_by_crm(job.doctor_crm)
    
        if self.__checkIfExistsJobScheduledToDepartmentAndDate(job.department, job.date, job.period):
            raise HTTPException(status_code=400, detail="Job can not be scheduled")
        else:
            if doctor.isActive:
                self.jobs.append(job)
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

    def __checkIfExistsJobScheduledToDepartmentPeriodAndDate(self, department, date, period):
        if len(self.jobs) > 0: 
            for job in self.jobs:
                if job.department == department and job.date == date and job.period == period:
                    return True
                else:
                    return False
        else:
            return False