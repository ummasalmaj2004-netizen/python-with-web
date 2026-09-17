from fastapi import FastAPI

app = FastAPI(
    title="Student Task Manager",
    description="A simple web application built with Python and FastAPI.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Task Manager!"
    }
