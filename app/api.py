from fastapi import FastAPI, Request
from app.functions import gerarArquivo, informacoesArquivo
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import csv
import os

templates = Jinja2Templates(directory='templates')
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/gerar")
def gerar():
    dados = gerarArquivo()
    nome_arquivo = "mockInfo.csv"
    
    with open("mockInfo.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'CPF', 'Data de nascimento', 'Telefone', 'Endereço', 'Email'])
        writer.writerows(informacoesArquivo)

    return FileResponse(path=nome_arquivo, filename=nome_arquivo, media_type='text/csv', background=lambda: os.remove('mockInfo.csv'))