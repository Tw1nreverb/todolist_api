from fastapi import FastAPI
from src.task_router import router as task_router
app = FastAPI()
app.include_router(task_router)
