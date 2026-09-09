import os
os.system("cls")

menu = '''
+--------+--------------------+------------+

| Código | Prato              | Preço      |
+--------+--------------------+------------+

|   1    | Picanha            | R$ 25,00   |
|   2    | Lasanha            | R$ 20,00   |
|   3    | Strogonoff         | R$ 18,00   |
|   4    | Bife Acebolado     | R$ 15,00   |
|   5    | Pão com ovo        | R$ 5,00    |
+--------+--------------------+------------+
'''
print(menu)

codigo = input("Selecione o código do prato desejado: ")

print("\n-- SELEÇÃO --")
match codigo:
    case "1":
        print("Você escolheu: Picanha - R$ 25,00")
    case "2":
        print("Você escolheu: Lasanha - R$ 20,00")
    case "3":
        print("Você escolheu: Strogonoff - R$ 18,00")
    case "4":
        print("Você escolheu: Bife Acebolado - R$ 15,00")
    case "5":
        print("Você escolheu: Pão com ovo - R$ 5,00")
    case _:
        print("Não há esta opção de prato")
