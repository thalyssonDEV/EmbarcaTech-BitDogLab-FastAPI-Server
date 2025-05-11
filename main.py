from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

import uvicorn

app = FastAPI()

last_data = {}

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.api_route("/data", methods=["GET", "POST"])
async def receber_dados(request: Request):
    global last_data

    if request.method == "POST":

        body = await request.json()
        print("Dados Recebidos (POST):", body)

        processed_data = {
            "direction": body.get("direction"),
            "vrx": body.get("vrx"),
            "vry": body.get("vry"),
            "button_status": body.get("button_status"),
            "sensor_status": body.get("sensor_status")
        }

        last_data = processed_data

        return {"status": "ok"}
    
    else: 
        return JSONResponse(content=last_data)


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
