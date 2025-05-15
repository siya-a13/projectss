from fastapi import FastAPI, Request  # type: ignore
from apscheduler.schedulers.background import BackgroundScheduler  # type: ignore
from apscheduler.triggers.cron import CronTrigger # type: ignore
from datetime import datetime
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

CRON_MINUTE = os.getenv("CRON_MINUTE", "*/1")  # default: every 1 min

app = FastAPI()
scheduler = BackgroundScheduler()

def my_cron_job():
    print(f"[{datetime.now()}] Cron job executed!")

@app.on_event("startup")
def start_scheduler():
    print(f"Starting job with CRON_MINUTE={CRON_MINUTE}")
    scheduler.add_job(my_cron_job, CronTrigger(minute=CRON_MINUTE))
    scheduler.start()

@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown()

@app.get("/")
def root():
    return {"message": "FastAPI with cron job and env variable"}

@app.post("/task")
async def create_task(request: Request):
    data = await request.json()
    print(f"[{datetime.now()}] POST /task received with data: {data}")
    return {"message": "Task received successfully!", "data": data}
