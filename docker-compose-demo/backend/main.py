from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from redis import Redis
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
mongodb_client = AsyncIOMotorClient(os.getenv("MONGODB_URL", "mongodb://mongodb:27017"))
db = mongodb_client.taskdb

# Redis connection
redis_client = Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

@app.get("/")
async def read_root():
    return {"message": "Task Management API"}

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    try:
        # First, try to create in MongoDB
        task_dict = task.dict()
        result = await db.tasks.insert_one(task_dict)
        task_dict['_id'] = str(result.inserted_id)
        
        # Then cache in Redis
        redis_client.setex(
            f"task:{result.inserted_id}",
            3600,  # Cache for 1 hour
            json.dumps(task_dict)
        )
        
        return task_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    try:
        tasks = []
        async for task in db.tasks.find():
            task['_id'] = str(task['_id'])
            tasks.append(task)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    try:
        # Try to get from cache first
        cached_task = redis_client.get(f"task:{task_id}")
        if cached_task:
            return json.loads(cached_task)
        
        # If not in cache, get from MongoDB
        task = await db.tasks.find_one({"_id": task_id})
        if task:
            task['_id'] = str(task['_id'])
            return task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
