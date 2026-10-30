import os
os.system("cls")

menu = '''
+--------+----------------------+------------+
|                                            |
| Código | Item                 | Valor      |
+--------+----------------------+------------+
|                                            |
| 1      | Picanha              | R$ 24,99   |
| 2      | Lasanha              | R$ 19,99   |
| 3      | Strogonoff           | R$ 17,99   |
| 4      | Bife Acebolado       | R$ 14,99   |
| 5      | Pão com ovo          | R$  4,99   |
| 6      | Hamburguer Artesanal | R$ 21,99   |
| 7      | Batata Frita Grande  | R$ 11,99   |
| 8      | Refrigerante Lata    | R$  5,99   |
| 9      | Suco Natural         | R$  7,99   |
| 10     | Pudim de Leite       | R$  6,99   |
+--------+----------------------+------------+
'''

produtos = [
    "Picanha", "Lasanha", "Strogonoff", "Bife Acebolado", "Pão com ovo",
    "Hamburguer Artesanal", "Batata Frita Grande", "Refrigerante Lata", "Suco Natural", "Pudim de Leite"
]
precos = [24.99, 19.99, 17.99, 14.99, 4.99, 21.99, 11.99, 5.99, 7.99, 6.99]

pratos_escolhidos = []
valores_escolhidos = []
total_conta = 0.0

continuar = "S"

while continuar == "S" or continuar == "s":
    os.system("cls")
    print(menu)
    
    opcao = int(input("Digite o código do item desejado (1 a 10): "))
    
    if opcao >= 1 and opcao <= 10:
        indice = opcao - 1
        pratos_escolhidos.append(produtos[indice])
        valores_escolhidos.append(precos[indice])
        total_conta += precos[indice]
    else:
        print("Opção inválida! Nenhum item foi adicionado.")
        
    continuar = input("\nDeseja escolher outro item? (S/N): ")

os.system("cls")
print("--- PEDIDOS REALIZADOS ---")

posicao = 0
for prato in pratos_escolhidos:
    valor = valores_escolhidos[posicao]
    print(f"• {prato}: R$ {valor:.2f}")
    posicao += 1

print("-" * 35)
print(f"VALOR TOTAL: R$ {total_conta:.2f}")