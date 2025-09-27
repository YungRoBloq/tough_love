#API To Receive Data
from fastapi import FastAPI, Request
import database_functions
import uvicorn 

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


