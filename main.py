from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    storage_path = "/mnt/storage"
    exists = os.path.exists(storage_path)
    return {
        "message": "Hello World from asdfhgjhj!",
        "storage_mounted": exists,
        "storage_path": storage_path
    }
