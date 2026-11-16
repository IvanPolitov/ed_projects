from enum import Enum
from fastapi import FastAPI, HTTPException

app = FastAPI()


from pydantic import BaseModel

class JobStatus(Enum):
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELLED = 'CANCELLED'

class JobType(Enum):
    SLEEP = 'sleep'
    HTTP_REQUEST = 'http_request'
    URL_CHECK = 'url_check'
    BATCH_HTTP = 'batch_http'

class JobCreate(BaseModel):
    type: JobType
    params: dict

class Job(JobCreate):
    job_id: int
    status: JobStatus = JobStatus.PENDING
    result: dict | None = None
    error: str | None = None


test_arr = []
current_id = 1

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/jobs")
def create_job(job: JobCreate):
    global current_id
    new_job = Job(job_id=current_id, type=job.type, params=job.params)
    current_id += 1
    test_arr.append(new_job)
    return {"job": new_job}


@app.get("/jobs")
def read_jobs():
    return {"jobs": test_arr}


@app.get("/jobs/{job_id}")
def read_job(job_id: int):
    for job in test_arr:
        if job.job_id == job_id:
            return {"job": job}
    raise HTTPException(status_code=404, detail="Job not found")


@app.post("/jobs/{job_id}/cancel")
def cancel_job(job_id: int):
    for job in test_arr:
        if job.job_id == job_id:
            job.status = JobStatus.CANCELLED
            return {"message": 'Job CANCELLED', "job": job}
    raise HTTPException(status_code=404, detail="Job not found")