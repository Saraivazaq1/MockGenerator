from fastapi import FastAPI
from app.functions import gerarArquivo

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/gerar')
async def gerar():
    dados = gerarArquivo()
    return dados