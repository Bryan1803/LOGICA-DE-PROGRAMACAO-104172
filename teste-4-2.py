import os
import time

os.system("cls")

def mostrar_tabuada(numero):
    print(f"\n= TABUADA DO {numero} =")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        time.sleep(1.2)

while True:
    numero = int(input("Digite um número de 1 a 10: "))
    if 1 <= numero <= 10:
        break
    else:
        print("Número inválido! Digite apenas um valor entre 1 e 10.\n")

mostrar_tabuada(numero)