from unicodedata import name
from src.infra.repo.user_repository import UserRepository
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home")
def home():
    return(
        "%s top %s dms"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, access_log=False)