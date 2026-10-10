import uvicorn
from fastapi import FastAPI
from app.practice_api01 import router as practice_api01
from app.practice_api02 import router as practice_api02
from app.practice_api03 import router as practice_api03
from app.practice_api04 import router as practice_api04

app = FastAPI()
app.include_router(practice_api01)
app.include_router(practice_api02)
app.include_router(practice_api03)
app.include_router(practice_api04)



@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)