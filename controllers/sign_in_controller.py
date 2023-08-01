from moduls import security
from datetime import datetime, timedelta
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status, Request, Response, encoders,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, \
    OAuth2
sign_in_router = APIRouter()

@sign_in_router.post("/login", response_model=security.Token)
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = security.authenticate_user(security.tecniquies, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
        httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}