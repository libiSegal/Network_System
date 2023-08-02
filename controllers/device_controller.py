from fastapi import APIRouter, Depends, HTTPException
from moduls import devices_handle
from moduls import security

device_router = APIRouter()


@device_router.get("/network/{network_id}/devices/")
async def get_devices(network_id, current_user: security.User = Depends(security.get_current_active_user)):
    if not network_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    return devices_handle.get_all_devices(network_id)


@device_router.get("/{client_id}/devices/")
async def get_network_data(client_id, current_user: security.User = Depends(security.get_current_active_user)):
    if not client_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    return devices_handle.get_devices_by_client_id(client_id)


@device_router.get("/network/{network_id}/filter-devices/")
async def get_filtering_devices(network_id, vendor: str = '',
                                current_user: security.User = Depends(security.get_current_active_user)):
    if not network_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    return devices_handle.get_devices_by_vendor(network_id, vendor)
