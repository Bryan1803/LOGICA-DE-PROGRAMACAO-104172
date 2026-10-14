import os
os.system("cls")

print("= INSERINDO NOTAS NO VETOR =")
vetor_notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    vetor_notas.append(nota)


print("\n= EXIBINDO NOTAS =")
for indice, numero in enumerate(vetor_notas, start=1):
    print(f"{indice}ª nota: {numero:.1f}")

soma = sum(vetor_notas)
media = soma / 4

print(f"\nMédia final: {media:.1f}")

print("\n= SITUAÇÃO DO ALUNO =")
if media >= 7.0:
    print("Aprovado")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Reprovado")