from moduls import network_handle
from moduls import cap_file_analyze
import uvicorn
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


# api/network/?path=""&user=""..
@app.post("/upload")
async def upload_pcap_file(file: UploadFile = File(...)):
    # Check if a file was provided in the request
    if not file:
        return 'No file uploaded', 400
    pkts = cap_file_analyze.get_packets(file)
    print(cap_file_analyze.get_all_devices(pkts))
    return f'File{file.filename} uploaded successfully'


@app.get("/network/{network_id}/communication")
async def get_network_communication(network_id):
    return "קריאה לפונקציה ששולפת"


# Maybe we need to return also the devices?
@app.get("/network/{network_id}")
async def get_network_details(network_id):
    return network_handle.get_network_details(network_id)


uvicorn.run(app, host="127.0.0.1", port=8000)
