



from fastapi import FastAPI, UploadFile, File
import uvicorn
app = FastAPI()

# api/network/?path=""&user=""..
@app.post("/upload")
async def upload_pcap_file(file: UploadFile = File(...)):
    # Check if a file was provided in the request
    if not file:
        return 'No file uploaded', 400
    return f'File{file.filename} uploaded successfully'
@app.get("/network/{network_id}/communication")
async def get_network_communication(network_id):
    return "קריאה לפונקציה ששולפת"

# api/netwok/user_id|network_id
@app.get("/network/{user_id}/{network_id}")
async def get_network_data(user_id,network_id):
    return "קריאה לפונקציה ששולפת"

uvicorn.run(app, host="0.0.0.0", port=8000)