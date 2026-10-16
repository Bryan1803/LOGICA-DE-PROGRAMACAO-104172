import os
os.system("cls")

vetor = []

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    
    if numero < 0:
        numero = 0
        
    vetor.append(numero)

print("\n--- Valores do Vetor ---")
for posicao, numero in enumerate(vetor, start=1):
    print(f"Posição {posicao}: {numero}")