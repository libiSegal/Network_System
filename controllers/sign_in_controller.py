#api/signIn/token|id

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()
security = HTTPBasic()

@app.get("/profile")
async def main(credentials: HTTPBasicCredentials = Depends(security)):
    return {"name": "John Smith"}

uvicorn.run(app, host="localhost", port=8000)
