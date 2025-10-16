# Calculador de gorjeta

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")


# Classificador de palindromo

def eh_palindromo(texto: str) -> str:
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite uma palavra ou frase: ")
print(eh_palindromo(frase))


# Calculador de produto

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"Preço final com desconto: R$ {preco_final:.2f}")


# Tempo de pessoa viva

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.today()

dias_vividos = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vividos} dias.")
