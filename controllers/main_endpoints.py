import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from controllers import network_controller, device_controller

app = FastAPI()

app.include_router(network_controller, prefix="/networks", tags=["networks"],)
app.include_router(device_controller, prefix="/technicians", tags=["technicians"],)


uvicorn.run(app, host="127.0.0.1", port=8000)
