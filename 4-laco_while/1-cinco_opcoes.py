import os
os.system("cls")

menu = '''
+------+-----------------+------------+

| Produto         | Preço      |      |
+------+-----------------+------------+

| 1    | Espaguete       | R$  8,00   |
| 2    | Pizza           | R$  14,90  |
| 3    | Pão de Queijo   | R$  4,50   |
| 4    | Bolacha         | R$ 6,00    |
| 5    | Bolo de milho   | R$  8,00   |
+------+-----------------+------------+
'''
print(menu)

opcao = int(input("Digite o código do item desejado (1 a 5): "))

item_escolhido = ""
preco_escolhido = 0.0

if opcao == 1:
    item_escolhido = "Espaguete"
    preco_escolhido = 8.00
elif opcao == 2:
    item_escolhido = "Pizza"
    preco_escolhido = 14.90
elif opcao == 3:
    item_escolhido = "Pão de Queijo"
    preco_escolhido = 4.50
elif opcao == 4:
    item_escolhido = "bolacha"
    preco_escolhido = 6.00
elif opcao == 5:
    item_escolhido = "Bolo de milho"
    preco_escolhido = 8.00
else:
    print("Opção inválida!")

if opcao >= 1 and opcao <= 5:
    os.system("cls")
    print(f"Opção Escolhida: {item_escolhido}")
    print(f"Preço: R$ {preco_escolhido:.2f}")
