# Arquivo principal

from app.functions import gerarLinha, informacoesArquivo
from os import system, name
import csv

# TODO: Disponibilizar o download de um arquivo csv com as informações geradas
# TODO: Comentar o código, fazer ajustes de formatação e otimizar


# Interface no terminal para o usuário
while True:
    print(
        """
[1] - Gerar lista
[2] - Sair
"""
    )

    escolha = input("Escolha um número de 1 a 2: ")

    i = 0
    match escolha:
        case "1":
            linhasNum = int(input("Quantas linha terá o arquivo? "))
            for x in range(linhasNum):
                gerarLinha()
                print(informacoesArquivo[x])

            # Criando o arquivo .csv com as informações geradas
            with open("mockInfo.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(informacoesArquivo)

        case "2":
            break

        case _:
            system('cls' if name == 'nt' else 'clear')
            print("Digite uma opção válida")
