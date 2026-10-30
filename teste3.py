import os

lista_produtos = []

while True:
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela no Windows e Linux/Mac
    print('''
    == MERCADINHO BIG BOM ==
    1- Cadastrar produto
    2- Listar todos os produtos
    3- Atualizar produto
    4- Remover produto
    5- Buscar produto
    6- Sair
    ''')
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        input("\nPressione Enter para continuar...")
        continue

    match opcao:
        case 1:
            nome = input("Nome do produto: ").strip()
            if any(p['nome'].lower() == nome.lower() for p in lista_produtos):
                print("Produto já cadastrado!")
            else:
                preco = float(input("Preço do produto: R$ "))
                lista_produtos.append({"nome": nome, "preco": preco})
                print(f"'{nome}' cadastrado com sucesso!")
            input("\nPressione Enter para continuar...")

        case 2:
            print("\n=== LISTA DE PRODUTOS ===")
            if not lista_produtos:
                print("Nenhum produto cadastrado.")
            else:
                for i, produto in enumerate(lista_produtos, 1):
                    print(f"{i}. {produto['nome']} - R$ {produto['preco']:.2f}")
            input("\nPressione Enter para continuar...")

        case 3:
            nome_busca = input("Nome do produto que deseja atualizar: ").strip()
            encontrado = False
            for produto in lista_produtos:
                if produto['nome'].lower() == nome_busca.lower():
                    produto['nome'] = input("Novo nome do produto: ").strip()
                    produto['preco'] = float(input("Novo preço do produto: R$ "))
                    print("Produto atualizado com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado!")
            input("\nPressione Enter para continuar...")

        case 4:
            nome_busca = input("Nome do produto que deseja remover: ").strip()
            encontrado = False
            for produto in lista_produtos:
                if produto['nome'].lower() == nome_busca.lower():
                    lista_produtos.remove(produto)
                    print("Produto removido com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado!")
            input("\nPressione Enter para continuar...")

        case 5:
            nome_busca = input("Nome do produto que deseja buscar: ").strip()
            encontrado = False
            for produto in lista_produtos:
                if produto['nome'].lower() == nome_busca.lower():
                    print(f"\nProduto Encontrado: {produto['nome']} - R$ {produto['preco']:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado!")
            input("\nPressione Enter para continuar...")

        case 6:
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida! \nTente novamente...")
            input("\nPressione Enter para continuar...")
            continue