import os
os.system("cls")

QUANTIDADE_REPETICOES = 3
pares = 0
impares = 0

for i in range(QUANTIDADE_REPETICOES):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares = pares + 1
else:
    impares = impares + 1

print(f"\nQuantidade de pares: {pares}")
print(f"\nQuantidade de ímpares: {impares}")

print("\nFIM")