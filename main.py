from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend (React) to communicate with backend
app.add_middleware(
    CORSMiddleware,
    # Allows all origins, change to ["http://localhost:3000"] for security
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []  # Storing tasks temporarily in memory


class Task(BaseModel):
    text: str


@app.get("/tasks", response_model=List[dict])
def get_tasks():
    return tasks  # Return all tasks stored


@app.post("/add_task")
def add_task(task: Task):
    tasks.append({"id": len(tasks) + 1, "text": task.text})
    return {"message": "Task added!", "task": task.text}


# Run FastAPI server (only needed if running as a script)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
