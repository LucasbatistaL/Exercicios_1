# Gerador de senhas

import random
import string

tamanho = int(input("Digite o tamanho da senha desejada: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")


# Buscador de usuario

import requests

try:
    resposta = requests.get("https://randomuser.me/api/")
    resposta.raise_for_status()  # Garante que erros HTTP sejam tratados
    dados = resposta.json()

    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except requests.RequestException:
    print("Falha na conexão. Não foi possível acessar a API.")



# Consultador de CEP

cep = input("Digite o CEP (apenas números): ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    resposta.raise_for_status()
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")

except requests.RequestException:
    print("Falha na conexão. Não foi possível acessar a API.")



# Consulte informações em relação ao real

try:
    resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
    resposta.raise_for_status()
    dados = resposta.json()

    if "USDBRL" in dados:
        cotacao = dados["USDBRL"]
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Máxima: R$ {cotacao['high']}")
        print(f"Mínima: R$ {cotacao['low']}")
        print(f"Data/Hora da última atualização: {cotacao['create_date']}")
    else:
        print("Moeda não encontrada na API.")

except requests.RequestException:
    print("Falha na conexão. Não foi possível acessar a API.")
