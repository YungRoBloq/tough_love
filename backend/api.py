#API To Receive Data
from fastapi import FastAPI, Request
import uvicorn 

app = FastAPI()

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    return {"status": "success", 
            "received": data}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


