from moduls import network_handle
from moduls import communication_handle
from fastapi import APIRouter, UploadFile, File, Form

network_router = APIRouter()


@network_router.post("/upload")
async def upload_pcap_file(file: UploadFile = File(...),
                           client_id: str = Form(...),
                           location: str = Form(...)):
    # Check if a file was provided in the request
    if not file:
        return 'No file uploaded', 400
    network_handle.create_network(file, client_id, location)
    return f'File{file.filename} uploaded successfully'


@network_router.get("{network_id}/communication")
async def get_network_communication(network_id):
    return communication_handle.get_communication(network_id)


@network_router.get("/{network_id}")
async def get_network_details(network_id):
    return network_handle.get_network_data(network_id)

