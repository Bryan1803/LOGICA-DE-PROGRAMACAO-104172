import os
os.system("cls")

vetor = []
qtd_negativos = 0
soma_positivos = 0

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    vetor.append(numero)

    if numero > 0:
        soma_positivos += numero
    
    if numero % 2 == 1:
        soma_positivos += numero

print("\n--- Resultado ---")
print(f"Vetores: {vetor}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")