import os
import time
os.system("cls")
soma = 0

for i in range(5):
    numero = int(input(f"\nDigite o {i+1}º número inteiro: "))
    soma = numero + soma

print(f"\nA soma de todos os números lidos é: {soma}")

print("\nFIM")