import os
os.system("cls")

print("= INSERINDO NOTAS NO VETOR =")
vetor_notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    vetor_notas.append(nota)


print("\n= EXIBINDO NOTAS =")
for indice, nota in enumerate(vetor_notas, start=1):
    print(f"{indice}ª nota: {nota:.1f}")

soma = sum(vetor_notas) #Somar tudo que está no vetor
media = soma / 3

print(f"\nMédia final: {media:.1f}")