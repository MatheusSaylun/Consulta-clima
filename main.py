from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restrinja isso
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "insira sua API"

@app.get("/clima/{cidade}")
def obter_clima(cidade: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        return {"erro": "Cidade não encontrada"}

    dados = resposta.json()
    clima = {
        "cidade": dados["name"],
        "pais": dados["sys"]["country"],
        "temperatura": dados["main"]["temp"],
        "descricao": dados["weather"][0]["description"]
    }
    return clima

