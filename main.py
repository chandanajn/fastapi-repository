from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI application deployed on AWS using Docker"
    }

@app.get("/about")
def about():
    return {
        "course": "AWS Deployment",
        "framework": "FastAPI"
    }