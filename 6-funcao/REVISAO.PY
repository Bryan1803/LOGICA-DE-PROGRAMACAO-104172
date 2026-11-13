import os
os.system("cls")

# Função sem retorno e sem parâmetros
def logo_senai():
    os.system("cls")
    print('\n==================')
    print('      SENAI       ')
    print('==================')

# Função sem retorno e com parâmetros
def mostrar_dados(nome, idade):
    print(f"{nome} tem {idade} anos.")

# Chama a função para limpar a tela e mostrar o logo
logo_senai()
print("\n= Solicitando dados =")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Limpa a tela novamente e exibe os resultados
logo_senai()
print("\n= EXIBINDO DADOS =")
mostrar_dados(nome, idade)