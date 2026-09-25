import os
import time
os.system("cls")

soma = 0

print(f"Valor INICIAL da variável soma: {soma}")

for i in range(3):
    soma += int(input(f"\nDigite um número para somar: "))

print(f"\nValor FINAL da variável soma: {soma}")