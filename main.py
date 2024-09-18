from fastapi import FastAPI
from src.task_router import router as task_router
from src.user_router import router as user_router
import uvicorn

app = FastAPI()
app.include_router(task_router)
app.include_router(user_router)
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
