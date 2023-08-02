from moduls import network_handle
from moduls import communication_handle
from moduls import network_visualization
from moduls import security
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
import io
import PIL.Image as Image

from moduls.Exception import AuthorizationError

network_router = APIRouter()


@network_router.post("/upload")
async def upload_pcap_file(file: UploadFile = File(...),
                           client_id: str = Form(...),
                           location: str = Form(...),
                           current_user: security.User = Depends(security.get_current_active_user)):
    # Check if a file was provided in the request
    if not file:
        raise HTTPException(400, 'No file uploaded')
    try:
        network_handle.create_network(file, client_id, location, current_user.id)
        return f'File{file.filename} uploaded successfully'
    except AuthorizationError as e:
        return str(e)


@network_router.get("/{network_id}/communication")
async def get_network_communication(network_id,
                                    current_user: security.User = Depends(security.get_current_active_user)):
    # client_network = network_handle.get_network_client(network_id)
    # return client_network
    if not network_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    return communication_handle.get_communication(network_id)



@network_router.get("/{network_id}")
async def get_network_details(network_id):
    if not network_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    return network_handle.get_network_data(network_id)


@network_router.get('/{network_id}/visual')
async def visual(network_id):
    if not network_id.isdecimal():
        raise HTTPException(400, 'Invalid input')
    network_visualization.get_visual(network_id)
    return FileResponse('graf.png')
