import os
os.system("cls")
from colorama import init, Fore, Back, Style

# O 'autoreset=True' faz com que a cor volte ao normal automaticamente no final de cada print!
init(autoreset=True)

# Entrada de dados
valor_produto = float(input(f"{Style.BRIGHT}Informe o valor do produto: R$ "))

print(f"\n{Fore.BLUE}{Style.BRIGHT}Escolha a forma de pagamento:")
print(f"{Fore.BLUE}1 - Pagamento à vista")
print(f"{Fore.BLUE}2 - Pagamento à prazo")
forma_pagamento = int(input(f"{Style.BRIGHT}Opção: "))

print(f"{Fore.YELLOW}-" * 40)

# Estrutura principal usando MATCH-CASE
match forma_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        valor_final = valor_produto - desconto
        print(f"{Fore.GREEN}{Style.BRIGHT}Se o pagamento for à vista:")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: {Fore.GREEN}R$ {desconto:.2f}")
        print(f"Total a pagar: {Fore.GREEN}{Style.BRIGHT}R$ {valor_final:.2f}")
        
    case 2:
        parcelas = int(input(f"{Style.BRIGHT}Digite a quantidade de parcelas (em até 6 vezes): "))
        
        # Uso do 'if' dentro do match para validar o intervalo de 1 a 6
        match parcelas:
            case p if 1 <= p <= 6:
                valor_parcela = valor_produto / parcelas
                print(f"\n{Fore.GREEN}{Style.BRIGHT}Se o pagamento for à prazo:")
                print(f"Valor do produto: R$ {valor_produto:.2f}")
                print("Forma de pagamento: à prazo")
                print(f"Quantidade de parcelas: {parcelas}x")
                print(f"Valor por parcela: {Fore.GREEN}R$ {valor_parcela:.2f}")
                print(f"Total à prazo: {Fore.GREEN}{Style.BRIGHT}R$ {valor_produto:.2f}")
            case _:
                print(f"{Fore.RED}{Style.BRIGHT}Erro: Quantidade de parcelas inválida! Permitido apenas até 6 vezes.")
                
    case _:
        print(f"{Fore.RED}{Style.BRIGHT}Erro: Opção de pagamento inválida.")