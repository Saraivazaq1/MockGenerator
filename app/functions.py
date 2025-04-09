# Funções gerais

from faker import Faker
import random
import csv

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
def gerarArquivo():

    for x in range(10):
        nome = fake.name()
        cpf = gerarCpf()
        dataNascimento = fake.date_of_birth().strftime("%d/%m/%Y")
        telefone = fake.phone_number()
        endereco = fake.address()
        email = fake.email()
        
        informacoesArquivo.append([nome, cpf, dataNascimento, telefone, endereco, email])

    with open("mockInfo.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'CPF', 'Data de nascimento', 'Telefone', 'Endereço', 'Email'])
        writer.writerows(informacoesArquivo)