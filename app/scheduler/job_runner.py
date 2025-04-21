# app/scheduler/job_runner.py
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.bank_fetcher import fetch_bank_transactions

def start_scheduler():
    scheduler = BackgroundScheduler(timezone="Africa/Johannesburg")
    scheduler.add_job(fetch_bank_transactions, 'cron', hour=0, minute=0, id="bank-fetch-job")
    scheduler.start()
    print("🕛 Scheduler started: bank-fetch-job scheduled for midnight")
