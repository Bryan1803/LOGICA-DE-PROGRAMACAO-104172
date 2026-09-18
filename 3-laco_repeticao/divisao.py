import os
os.system("cls")

print("= TABUADA =")
numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero / i
    print(f"{numero} / {i} = {resultado:.2f}")

print("FIM DO PROGRAMA. ")
