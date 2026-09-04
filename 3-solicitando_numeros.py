import os
os.system("cls")

nome = input("Digite seu nome: ")
numero = int(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print(f"Olá {nome}, o número {numero} está entre 10 e 20")