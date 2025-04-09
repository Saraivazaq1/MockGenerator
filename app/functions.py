# Funções gerais

from faker import Faker
import random

# Instância do Faker
fake = Faker()

# Array com as informações
informacoesArquivo = []

# Lógica da geração de um cpf
def gerarCpf():
    cpf = [random.randint(0, 9) for _ in range(9)]

    soma = sum((10 - i) * cpf[i] for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10
    cpf.append(primeiro_digito)

    soma = sum((11 - i) * cpf[i] for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10
    cpf.append(segundo_digito)

    return f'{''.join(map(str, cpf))}'

# Geração de uma linha no arquivo .csv
def gerarLinha():
    linha = []
    linha.append(fake.name())
    linha.append(gerarCpf())
    linha.append(fake.date_of_birth().strftime("%d/%m/%Y"))
    linha.append(fake.phone_number())
    linha.append(fake.address())
    linha.append(fake.safe_email())
    
    informacoesArquivo.append(linha)