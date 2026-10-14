import os
os.system("cls")

print("= INSERINDO NÚMEROS NO VETOR =")
vetor_numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor_numeros.append(numero)


print("\n= EXIBINDO NÚMEROS =")
for indice, numero in enumerate(vetor_numeros, start=1):
    print(f"{indice}º número: {numero}")

maior_numero = max(vetor_numeros)
menor_numero = min(vetor_numeros)

print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")