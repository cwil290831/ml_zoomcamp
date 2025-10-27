import uvicorn
from fastapi import FastAPI

app = FastAPI(title="ping")

@app.get("/ping")
def ping():
    return {"ping": "pong!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696) # run on local host and on port 969
