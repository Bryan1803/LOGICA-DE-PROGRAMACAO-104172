import os
os.system("cls")

menu = '''
+---------+----------------------------+

| Código  | Descrição                  |
|---------+----------------------------|
|    1    | Adicionar família          |
|    2    | Sair e exibir resultados   |
+---------+----------------------------+
'''

total_familias = 0
soma_salarios = 0
soma_filhos = 0

maior_salario = 0
menor_salario = 0

opcao = 1

while opcao < 2:
    print(menu)
    opcao = int(input("Digite o código da opção desejada: "))
    
    if opcao == 1:
        os.system("cls")
        
        salario = float(input("Digite o salário da família: R$ "))
        quantidade_filhos = int(input("Digite o número de filhos: "))
        
        if total_familias == 0:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario
                
        # Acumula os totais para as médias
        soma_salarios = soma_salarios + salario
        soma_filhos = soma_filhos + quantidade_filhos
        total_familias = total_familias + 1
        
        os.system("cls")

os.system("cls")
print("\n=== RESULTADOS DA PESQUISA ===")

if total_familias > 0:
    media_salario = soma_salarios / total_familias
    media_filhos = soma_filhos / total_familias
    
    print("a) Total de famílias que responderam:", total_familias)
    print("b) Média do salário da população: R$", media_salario)
    print("c) Média do número de filhos:", media_filhos)
    print("d) Maior salário: R$", maior_salario)
    print("e) Menor salário: R$", menor_salario)
else:
    print("Nenhuma família foi cadastrada.")

print("\n= PROGRAMA ENCERRADO =")