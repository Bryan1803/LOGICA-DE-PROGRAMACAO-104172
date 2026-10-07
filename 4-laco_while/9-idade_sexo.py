import os
os.system("cls")

menu = '''
+---------+-----------------+

| Código  | Descrição       |
|---------+-----------------|
|    1    | Adicionar pessoa|
|    2    |Exibir resultados|
|    3    |    Sair         |
+---------+-----------------+
'''

soma_salarios = 0
quantidade_pessoas = 0
mulheres_salario_alto = 0

maior_idade = 0
menor_idade = 0
opcao = 1

while opcao < 3:
    print(menu)
    opcao = int(input("Digite o código da opção desejada: "))
    
    if opcao == 1:
        os.system("cls")
        
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ")
        salario = float(input("Digite o salário: R$ "))
        
        if quantidade_pessoas == 0:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
                
        if sexo == "F":
            if salario >= 5000:
                mulheres_salario_alto = mulheres_salario_alto + 1
                
        soma_salarios = soma_salarios + salario
        quantidade_pessoas = quantidade_pessoas + 1
        
        os.system("cls")
        
    if opcao == 2:
        os.system("cls")
        print("\n=== RESULTADO ===")
        
        if quantidade_pessoas > 0:
            media_salario = soma_salarios / quantidade_pessoas
            print("a) Média de salário do grupo: R$", media_salario)
            print("b) Maior idade:", maior_idade, "| Menor idade:", menor_idade)
            print("c) Quantidade de mulheres com salário a partir de R$ 5.000,00:", mulheres_salario_alto)
        else:
            print("Nenhuma pessoa foi cadastrada ainda.")

print("\n= PROGRAMA ENCERRADO =")