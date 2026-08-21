import os
os.system("cls")

# SOLICITANDO DADOS
# input adiciona o que for digitado no terminal na variável como texto
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

#int() coverte o que foi digitado em inteiro (númerosd inteiros).
idade = int(input("Digite sua idade: "))

# float() converte o que foi digitado em float (numeros reais)
peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))

# MOSTRANDO DADOS.
print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print("Idade: ", idade)
print("Peso: ", peso)
print("Altura: ", altura)