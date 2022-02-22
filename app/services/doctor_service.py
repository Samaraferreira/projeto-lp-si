from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from ..models.doctor import Doctor
import json

class DoctorService:
    def __init__(self):
        self.doctors = self.__getData()
        
    def create(self, doctor: Doctor):
        if self.__checkIfCRMIsRegistered(doctor.crm):
            raise HTTPException(status_code=400, detail="Doctor CRM already registered")
        else:
            self.doctors.append(doctor)
            self.__saveData()
            return doctor

    def get_all(self):
        return self.doctors

    def get_by_crm(self, crm) -> Doctor:
        for doctor in self.doctors:
            if doctor.crm == crm:
                return doctor
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    def get_by_name(self, name) -> list[Doctor]:
        result = []
        for doctor in self.doctors:
            if name in doctor.name:
                result.append(doctor)
        if len(result) == 0: 
            raise HTTPException(status_code=404, detail="Doctor not found")
        else:
            return result

    def lock_doctor(self, crm): 
        if self.__checkIfCRMIsRegistered(crm):
            doctor = self.get_by_crm(crm)
            doctor.isActive = False
            return { "message": "Doctor was blocked"}
        else: 
            raise HTTPException(status_code=404, detail="CRM is not registered")
    
    def unlock_doctor(self, crm): 
        if self.__checkIfCRMIsRegistered(crm):
            doctor = self.get_by_crm(crm)
            doctor.isActive = True
            return { "message": "Doctor has been unlocked"}
        else: 
            raise HTTPException(status_code=404, detail="CRM is not registered")

    def __checkIfCRMIsRegistered(self, crm):
        if len(self.doctors) > 0: 
            for doctor in self.doctors:
                if doctor.crm == crm:
                    return True
        else:
            return False
    
    def __saveData(self):
        with open('app/data/doctors.json', 'w') as json_file:
            json.dump(jsonable_encoder(self.doctors), json_file)
    
    def __getData(self) -> list: 
        with open('app/data/doctors.json') as json_file:
            data_dict = json.load(json_file)
            return self.__parseToDoctor(data_dict)

    def __parseToDoctor(self, data_dict: dict):
        list = []
        for data in data_dict:
            doctor = Doctor(crm=data.get('crm'),name=data.get('name'),email=data.get('email'),
                            cpf=data.get('cpf'),phone=data.get('phone'),specialty=data.get('specialty'),isActive=data.get('isActive'))
            list.append(doctor)
        return list


service = DoctorService()