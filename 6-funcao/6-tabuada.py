import os
os.system("cls")

def mostrar_tabuada(numero):
    print(f"\n= TABUADA DO {numero} =")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para ver a tabuada: "))

mostrar_tabuada(numero)