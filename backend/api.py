#API To Receive Data
from fastapi import FastAPI, Request
import database_functions
from fastapi import FastAPI, Request, WebSocket
from contextlib import asynccontextmanager
import uvicorn 
import asyncio
import json
from datetime import datetime

shared_data = {
    "status": "active",
    "value": 42
}

test_data = {
    "id": 123,
    "name": "Test User",
    "email": "test@example.com",
    "roles": ["admin", "user"],
    "active": True,
    "timestamp": datetime.now().isoformat()
}

# Define the background loop function
async def loop():
    while True:
        shared_data["value"] += 1
        shared_data["time"] = datetime.now().astimezone().isoformat()
        await asyncio.sleep(1)

# Define lifespan with proper loop handling
@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(loop())
    try:
        yield  # Wait until the app is shutting down
    finally:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

# Create the app with the lifespan hook
app = FastAPI(lifespan=lifespan)

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            aq_data = database_functions.read_aq_data()
            uv_data = database_functions.read_uv_data()

            structure = {
                "aq_data": aq_data,
                "uv_data": uv_data
            } 


            await websocket.send_text(json.dumps(structure))
            print(f"Sent: {structure}")
            await asyncio.sleep(1)
    except Exception as e:
        print("WebSocket connection closed:", e)

# HTTP endpoint to receive data
@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()

    sensor_type = data["type"]

    if sensor_type == "uv":
        database_functions.write_uv_data(data)
    else:
        database_functions.write_aq_data(data)

    return {"status": "success", 
            "received": data}

# Run the app
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
