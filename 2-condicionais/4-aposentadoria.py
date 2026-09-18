import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA.
print("bem vindo ao inss ")
codigo = input ("Digite o código do empregado: ")
ano_do_nascimento = int(input ("Digite o ano de nascimento: "))
tempo_trabalho = int(input ("Digite o tempo de trabalho em anos: "))

# PROCESSAMENTO.
ano_atual = 2026
idade = ano_atual - ano_do_nascimento

if idade >= 65 or tempo_trabalho >= 30:
    print("É necessário aposentadoria")
else:
    print("Não é necessário aposentadoria")
# SAÍDA.
print("\n-- RESULTADO -- ")
print(f"Código do empregado: {codigo}")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_trabalho} anos")