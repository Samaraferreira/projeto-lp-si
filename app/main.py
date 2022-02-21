from fastapi import FastAPI, Depends

from .routes import doctors, jobs

app = FastAPI()

app.include_router(doctors.router)
app.include_router(jobs.router)