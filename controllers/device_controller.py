import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/network/{network_id}/devices/")
async def greet_user(network_id):
    return {"devices":"קריאה לפונקציה ששולפת את המכשירים לפי id של הרשת"}

uvicorn.run(app, host="localhost", port=8000)