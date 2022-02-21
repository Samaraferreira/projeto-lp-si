from fastapi import HTTPException
from ..models import doctor as Doctor
import json
from fastapi.encoders import jsonable_encoder

class DoctorService:
    # matrizes/listas
    def __init__(self):
        self.doctors = self.__getData()

    def create(self, doctor: Doctor):
        print(doctor)
        if self.__checkIfCRMIsRegistered(doctor.crm):
            raise HTTPException(status_code=400, detail="Doctor CRM already registered")
        else:
            self.doctors.append(doctor)
            self.__saveData(doctor)
            return doctor

    def get_all(self):
        return self.doctors

    # if/else and while/do..while e/ou for
    def get_by_crm(self, crm):
        for doctor in self.doctors:
            if doctor.crm == crm:
                return doctor
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    def get_by_name(self, name):
        result = []
        for doctor in self.doctors:
            if name in doctor.name:
                result.append(doctor)
        
        if len(result) == 0: 
            raise HTTPException(status_code=404, detail="Doctor not found")
        else:
            return result

    def __checkIfCRMIsRegistered(self, crm):
        if len(self.doctors) > 0: 
            for doctor in self.doctors:
                if doctor.crm == crm:
                    return True
                else:
                    return False
        else:
            return False
    
    def __saveData(self, doctor):
        list = []
        list.extend(self.__getData())
        list.append(doctor)
        with open('app/data/doctors.json', 'w') as json_file:
            json.dump(jsonable_encoder(list), json_file)
    
    def __getData(self): 
        with open('app/data/doctors.json') as json_file:
            data_dict = json.load(json_file)
            print(json.dump(data_dict))
            return json.dump(data_dict)