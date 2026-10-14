import os
os.system("cls")

print("= INSERINDO NÚMEROS NO VETOR =")
vetor_numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor_numeros.append(numero)


print("\n= EXIBINDO NÚMEROS =")
for indice, numero in enumerate(vetor_numeros, start=1):
    print(f"{indice}º número: {numero}")

pares = 0
impares = 0

for numero in vetor_numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")