
from fastapi import APIRouter
from moduls import devices_handle

device_router = APIRouter()


@device_router.get("/network/{network_id}/devices/")
async def get_devices(network_id):
    return devices_handle.get_all_devices(network_id)



