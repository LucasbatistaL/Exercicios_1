   Classificador de idade

idade =int(input("Digite sua idade: \n"))

if idade <= 12:
    print("Você é uma criança!")

elif idade > 12 and idade <=17:
    print('Você é um adolescente!')

elif idade >= 18 and idade <=59:
    print("Você é um adulto!")

else:
    print('Você é um idoso!')


    # Conversor de massa IMC

peso = float(input("Digite seu peso: "'\n'))
altura = float(input("Digite sua altura:"'\n'))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Abaixo do peso")

elif imc >= 18.6 and imc <= 25.5:
    print("Peso Normal")

elif imc <= 30 and imc >= 26:
    print("Sobrepeso")

else :
    print("Obeso")


# Conversor de Temperatura

t = float(input("Temperatura: "))
origem = input("De (C/F/K): ").upper()
destino = input("Para (C/F/K): ").upper()

if origem == destino:
    r = t
elif origem == "C" and destino == "F":
    r = t * 9/5 + 32
elif origem == "C" and destino == "K":
    r = t + 273.15
elif origem == "F" and destino == "C":
    r = (t - 32) * 5/9
elif origem == "F" and destino == "K":
    r = (t - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    r = t - 273.15
elif origem == "K" and destino == "F":
    r = (t - 273.15) * 9/5 + 32
else:
    print("Unidade inválida.")
    exit()

print(f"{t}°{origem} = {r:.2f}°{destino}")



 # Verificador de ano bissexto
 
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é bissexto !")
else:
    print(f"{ano} não é bissexto !")
