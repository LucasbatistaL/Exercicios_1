def calculadora():
    print("=== Calculadora Básica ===")
    print("Operações disponíveis: +  -  *  /")


    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))


    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero não é permitida.")
            return
    else:
        print("Operador inválido!")
        return

    print(f"Resultado: {resultado}")


calculadora()




 Programa de notas

notas = []
quantidade = int(input("Quantos alunos há na turma? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas dos alunos:")
for i, nota in enumerate(notas, start=1):
    print(f"Aluno {i}: {nota}")

print(f"\nMédia da turma: {media:.2f}")






Verificador de Senha

senha = input("Digite uma senha: ")

tamanho_valido = len(senha) >= 8
tem_numero = any(c.isdigit() for c in senha)

if tamanho_valido and tem_numero:
    print("Senha válida ✅")
else:
    print("Senha inválida ❌")





Classificador de Numero

quantidade = int(input("Quantos números deseja digitar? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é par")
    else:
        impares += 1
        print(f"{numero} é ímpar")

print(f"\nTotal de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
