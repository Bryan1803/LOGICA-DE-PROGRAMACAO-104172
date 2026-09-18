import os
os.system("cls")

media = float(input("Digite sua média: "))
faltas = int(input("Digite seu número de faltas: "))

print("\nCRITÉRIOS PARA A APROVAÇÃO")
print("\nMédia maior ou igual a 7.0")
print("Pode ter até 40 faltas")


if media >= 7 and faltas <= 40:
    print("\nO ALUNO FOI APROVADO!")

else:
    print("\nO ALUNO FOI REPROVADO!")