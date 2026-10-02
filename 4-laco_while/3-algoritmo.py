import os

os.system("cls")

while True:
    primeira_nota = float(input("\nDigite a primeira nota do aluno: "))
    if primeira_nota >= 0 and primeira_nota <= 10:
        
        segunda_nota = float(input("\nDigite a segunda nota do aluno: "))
        if segunda_nota >= 0 and segunda_nota <= 10:
            
            terceira_nota = float(input("\nDigite a terceira nota do aluno: "))
            if terceira_nota >= 0 and terceira_nota <= 10:
                break
            else:
                print("\nNota inválida, reiniciando o processo.")
        else:
            print("\nNota inválida, reiniciando o processo.")
    else:
        print("\nNota inválida, reiniciando o processo.")

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print(f"\nA média do aluno é: {media:.1f}")

if media >= 7:
    print("\nO aluno está aprovado.")
elif media >= 5 and media <= 6.9:
    print("\nO aluno está em recuperação.")
else:
    print("\nO aluno está reprovado.")

print("\n= FIM =")