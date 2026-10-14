import os
os.system("cls")

print("= INSERINDO NÚMEROS NO VETOR =")
vetor_notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    vetor_notas.append(nota)


print("\n= EXIBINDO NÚMEROS =")
for indice, numero in enumerate(vetor_notas, start=1):
    print(f"{indice}º: {numero}")