import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA.
print("bem vindo ao inss ")
matricula = input ("Digite a matricula do empregado: ")
ano_do_nascimento = int(input ("Digite o ano de nascimento: "))
tempo_trabalho = int(input ("Digite o tempo de trabalho em anos: "))

# PROCESSAMENTO.
ano_atual = 2026
idade = ano_atual - ano_do_nascimento

# SAÍDA.
print("\n-- RESULTADO -- ")
print(f"Matrícula do empregado: {matricula}")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_trabalho} anos")

if idade >= 65 or tempo_trabalho >= 30:
    print("Requer aposentadoria")
else:
    print("Não requer aposentadoria")