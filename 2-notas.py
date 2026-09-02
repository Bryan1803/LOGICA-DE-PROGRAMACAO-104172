import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA.
nome = input("Digite seu nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

# PROCESSAMENTO.
media= (nota1 + nota2)/2
if media >= 9:
    resultado= print(f"O aluno {nome} foi aprovado com avaliação A")

elif media >= 7.5 and media < 9:
    print(f"O aluno {nome} foi aprovado com avaliação B")

elif media >= 6 and media < 7.5:
    print(f"O aluno {nome} foi aprovado com avaliação C")

elif media >= 4 and media < 6:
    print(f"O aluno {nome} foi reprovado com avaliação D")

else:
    media < 4
    print(f"O aluno {nome} foi reprovado com avaliação E")

# SAÍDA.
print(f"")