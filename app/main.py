from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

import uvicorn

app = FastAPI()

last_data = {}

# Montar a pasta de arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Configuração do motor de templates
templates = Jinja2Templates(directory="app/templates")


@app.api_route("/data", methods=["GET", "POST"])
async def receber_dados(request: Request):
    global last_data

    if request.method == "POST":
        # Recebe os dados no formato JSON
        body = await request.json()
        print("Dados Recebidos (POST):", body)

        # Processa os dados recebidos e armazena em processed_data
        processed_data = {
            "direction": body.get("direction"),
            "vrx": body.get("vrx"),
            "vry": body.get("vry"),
            "button_status": body.get("button_status")
        }

        # Armazena os dados processados na variável global last_data
        last_data = processed_data

        # Retorna uma resposta indicando que os dados foram recebidos corretamente
        return {"status": "ok"}
    
    else:  # Se for GET
        # Retorna os dados mais recentes
        return JSONResponse(content=last_data)


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    print(f"\033[95mServidor FastAPI rodando...\033[0m")  # Cor roxa para "Servidor FastAPI"
    print(f"\033[93mAcesse a aplicação em:\033[0m")  # Cor amarela para o texto "Acesse"
    print(f"\033[1m\033[94m  -> http://127.0.0.1:8000\033[0m\n")  # Link em negrito e azul

    uvicorn.run(app, host="0.0.0.0", port=8000)