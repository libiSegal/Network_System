# api/signIn/token|id

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()
security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if not (credentials.username == "johnsmith") or not (credentials.password == "swordfish"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


@app.get("/profile")
async def main(username: str = Depends(get_current_username)):
    return {"username": username}


uvicorn.run(app, host="localhost", port=8000)
