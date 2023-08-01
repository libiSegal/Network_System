import uvicorn
from fastapi import FastAPI
from network_controller import network_router
from device_controller import device_router
from tachnician_controller import technician_router

app = FastAPI()

app.include_router(network_router, prefix="/network")
app.include_router(technician_router, prefix='/technician')
app.include_router(device_router)


uvicorn.run(app, host="127.0.0.1", port=8000)
