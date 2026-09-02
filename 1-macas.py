import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA.
quantidade = int(input ("Digite a quantidade de maçãs desejadas: "))

# PROCESSAMENTO.
if quantidade < 12:
    preco = 1.30

else:
    preco = 1.00

valor_total = quantidade * preco

# SAÍDA.
print(f"O valor total da compra é : R$ {valor_total}")
