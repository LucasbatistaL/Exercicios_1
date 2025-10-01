
from statistics import mean

# Conversor de Moeda

valor = float(input("Insira o valor desejado para conversão\n"))
dolar = round(valor * 5.20, 2)
euro = round(valor * 6.15, 2)
print(f"Seu valor em Dolar é: R${dolar}\nSeu valor em Euro é: R${euro}")



# Calculo de Desconto
nome  = input("nome do produto:")
produto = float(input("Insira o valor do produto: "))
desconto = produto * 0.2

print(f"Produto : {nome}\n Valor original:"
      f"R${produto}\n desconto: R${desconto}\n Valor final: R${produto - desconto}")


# Calculo Media

n1 = 7.5
n2 = 8.0
n3 = 6.5

media = mean([n1,n2,n3])
print(round(media, 2))


# calculo de combustivel

distancia = 300
combustivel = 25

media_por_km = round(300 / 25, 2)

print(f"Distancia: {distancia}km\ncombustivel gasto: {combustivel} litros\n"
      f"km rodado por litro:{media_por_km}km")
