import os
os.system("cls")
valor_produto = 0.0
valor_parcela = 0
parcelas = 0
valor_produto = float(input("Digite o valor do produto: R$ "))
menu = '''
+--------+--------------------+------------+
|                                          |
| Selecione a forma de pagamento  |        |
|--------+------------------------+        |
|                                          |
|   1    | Pagamento à vista      |        |
|   2    | Pagamento à prazo      |        |
+--------+------------------------+--------|
'''
print(menu)
forma_pagamento = float(input("Digite a opção: "))

match forma_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        total_a_pagar = valor_produto - desconto

        print("\nSe o pagamento for a vista:")
        print(f"Valor do produto: {valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total_a_pagar:.2f}")
    case 2:
        parcelas = int(input("Selecione a quanridade de parcelas (em até 6 vezes): "))
    case _:
        print("Quantidade de parcelas inválidas. O máximo é até 6 vezes")
match parcelas:
    case 1 | 2 | 3| 4| 5| 6:
        valor_parcela = valor_produto / parcelas

        print("\nSe o pagamento for à prazo:")
        print(f"Valor do produto: {valor_produto:.2f}")
        print("Forma de pagamento: à prazo")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor por parcela: {valor_parcela:.2f}")
        print(f"Total à prazo: R$ {valor_produto:.2f}")