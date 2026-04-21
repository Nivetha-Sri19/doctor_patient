from fastapi import FastAPI, HTTPException
from App.schemas import DoctorCreate, Doctor, PatientCreate, Patient
from App.database import doctors_db, patients_db

app = FastAPI()

# ---------------- DOCTOR APIs ---------------- #

@app.post("/doctors", response_model=Doctor)
def create_doctor(doctor: DoctorCreate):
    doctor_id = len(doctors_db) + 1
    new_doctor = doctor.dict()
    new_doctor["id"] = doctor_id

    doctors_db.append(new_doctor)
    return new_doctor


@app.get("/doctors", response_model=list[Doctor])
def get_doctors():
    return doctors_db


@app.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    for doctor in doctors_db:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(status_code=404, detail="Doctor not found")


# ---------------- PATIENT APIs ---------------- #

@app.post("/patients", response_model=Patient)
def create_patient(patient: PatientCreate):
    if patient.age <= 0:
        raise HTTPException(status_code=400, detail="Age must be greater than 0")

    patient_id = len(patients_db) + 1
    new_patient = patient.dict()
    new_patient["id"] = patient_id

    patients_db.append(new_patient)
    return new_patient


@app.get("/patients", response_model=list[Patient])
def get_patients():
    return patients_db