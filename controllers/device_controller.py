import uvicorn
from fastapi import FastAPI
from moduls import devices_handle

app = FastAPI()


@app.get("/network/{network_id}/devices/")
async def get_devices(network_id):
    return devices_handle.get_all_devices(network_id)


uvicorn.run(app, host="127.0.0.1", port=8000)
