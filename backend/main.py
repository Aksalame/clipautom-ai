from fastapi import FastAPI

app = FastAPI(
    title="ClipAutom AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ClipAutom AI 🚀"
    }
