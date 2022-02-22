from fastapi import FastAPI

from .routes import doctors, jobs

app = FastAPI()

app.include_router(doctors.router)
app.include_router(jobs.router)