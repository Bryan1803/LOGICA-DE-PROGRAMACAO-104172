import os 
os.system("cls")

# ENTRADA
print("= SOLICITANDO DADOS =")
salario_informado = float(input("Digite o valor do seu salário: "))

# PROCESSAMENTO
salario_minimo = 1621
quantidade_salarios = salario_informado / salario_minimo

# SAÍDA
print("\n= EXIBINDO DADOS =")
print(f"Quantidade de salários:  {quantidade_salarios:.2f}")