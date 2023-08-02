from flask import make_response, send_file

from moduls import network_handle
from moduls import communication_handle
from moduls import network_visualization
from moduls import security
from fastapi import APIRouter, UploadFile, File, Form, Depends
from fastapi.responses import FileResponse
import io
import PIL.Image as Image

network_router = APIRouter()


@network_router.post("/upload")
async def upload_pcap_file(file: UploadFile = File(...),
                           technician_id: str = Form(...),
                           client_id: str = Form(...),
                           location: str = Form(...),current_user: security.User = Depends(security.get_current_active_user)):
    # Check if a file was provided in the request
    if not file:
        return 'No file uploaded', 400
    network_handle.create_network(file, client_id, location, technician_id)
    return f'File{file.filename} uploaded successfully'


@network_router.get("{network_id}/communication")
async def get_network_communication(network_id,current_user: security.User = Depends(security.get_current_active_user)):
    return communication_handle.get_communication(network_id)


@network_router.get("/{network_id}")
async def get_network_details(network_id,current_user: security.User = Depends(security.get_current_active_user)):
    return network_handle.get_network_data(network_id)


@network_router.get('/{network_id}/visual')
async def a(network_id):
    network_visualization.get_visual(network_id)
    return FileResponse('graf.png')
