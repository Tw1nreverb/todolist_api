from fastapi import FastAPI
from src.task_router import router as task_router
import uvicorn

app = FastAPI()
app.include_router(task_router)
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
