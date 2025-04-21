# app/main.py
from fastapi import FastAPI
from app.routers import upload
from app.scheduler.job_runner import start_scheduler

app = FastAPI(title="WalletWise API")


@app.on_event("startup")
def on_startup():
    start_scheduler()

@app.get("/")
def root():
    return {"message": "WalletWise backend is running."}

app.include_router(upload.router)


