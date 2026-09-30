import os
os.system("cls")

while True:
    nota = float(input("\nDigite a nota do aluno: "))
    if nota < 0 or nota > 10:
        print("\n Nota inválida, tente novamente!")
    else:
        print(f"\nA nota do aluno é: {nota}")
        break

print("\n= FIM =")