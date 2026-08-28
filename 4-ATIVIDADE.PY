import os

# LIMPA O TERMINAL
os.system("cls")

#REGISTRO
usuario = input("Digite seu nome: ")

# ENTRADA
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"\nPrimeiro número: {numero1}")
print(f"Segundo número: {numero2}")
print(f"Terceiro número: {numero3}")
print(f"\nO maior número é: {maior}")
print(f"O menor número é: {menor}")