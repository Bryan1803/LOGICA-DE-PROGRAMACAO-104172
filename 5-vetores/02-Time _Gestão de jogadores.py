import os
os.system("cls")

# Apenas uma lista simples para guardar os jogadores como texto
jogadores = []

while True:
    print('''
    == GERENCIAMENTO DE ELENCO ==
    
    1. Cadastrar jogador
    2. Listar jogadores
    3. Atualizar jogador
    4. Excluir jogador
    0. Sair
    ''')
    
    opcao = input("Escolha uma opção: ")
    
    # --- 0. SAIR ---
    if opcao == "0":
        print("Saindo do sistema...")
        break
        
    # --- 1. CADASTRAR ---
    elif opcao == "1":
        os.system("cls")
        print("\n=== CADASTRAR JOGADOR ===")
        
        nome = input("\nNome do jogador: ")
        posicao = input("\nPosição: ").strip().upper()
        camisa = (input("\nNúmero da camisa: ")) # Lemos como texto para aceitar qualquer entrada
        
        # A única regra: se for apenas números, entra no cadastro
        if camisa.isnumeric():
            # Passamos por cada jogador da lista para ver se a camisa já existe
            camisa_ja_existe = False
            for j in jogadores:
                if "Camisa: " + camisa in j:
                    camisa_ja_existe = True
                    
            if camisa_ja_existe == True:
                print("\nErro: Essa camisa já está sendo usada por outro jogador!")
            else:
                # Se a camisa estiver livre, junta tudo e usa o append
                texto_jogador = nome + " | " + posicao + " | Camisa: " + camisa
                jogadores.append(texto_jogador)
                print("\nJogador cadastrado com sucesso!")
                
        # Se quem escrever colocar letras (Ex: AKAKAO), cai direto aqui no seu ELSE:
        else:
            print("\nColoque apenas números")
            
        input("\nPressione Enter para continuar...")
        os.system("cls")
        
    # --- 2. LISTAR ---
    elif opcao == "2":
        os.system("cls")
        print("=== LISTA DE JOGADORES ===")
        
        if len(jogadores) == 0:
            print("O elenco está vazio.")
        else:
            # Mostra a lista numerada de 1 até o final
            for i in range(len(jogadores)):
                print(f"{i + 1}. {jogadores[i]}")
                
        input("\nPressione Enter para continuar...")
        os.system("cls")
        
    # --- 3. ATUALIZAR ---
    elif opcao == "3":
        os.system("cls")
        print("=== ATUALIZAR JOGADOR ===")
        
        if len(jogadores) == 0:
            print("Não há jogadores para atualizar.")
        else:
            for i in range(len(jogadores)):
                print(f"{i + 1}. {jogadores[i]}")
                
            numero = int(input("\nDigite o número do jogador para alterar: "))
            indice = numero - 1
            
            novo_nome = input("\nDigite o novo nome: ")
            nova_posicao = input("\nDigite a nova posição: ").strip().upper()
            nova_camisa = input("\nDigite a nova camisa: ")
            
            # Substitui direto na posição da lista usando o índice
            jogadores[indice] = novo_nome + " | " + nova_posicao + " | Camisa: " + nova_camisa
            print("\nJogador atualizado com sucesso!")
            
        input("\nPressione Enter para continuar...")
        os.system("cls")
        
    # --- 4. EXCLUIR ---
    elif opcao == "4":
        os.system("cls")
        print("=== EXCLUIR JOGADOR ===")
        
        if len(jogadores) == 0:
            print("Não há jogadores para excluir.")
        else:
            for i in range(len(jogadores)):
                print(f"{i + 1}. {jogadores[i]}")
                
            numero = int(input("\nDigite o número do jogador para remover: "))
            indice = numero - 1
            
            # Descobre o texto do jogador escolhido
            jogador_escolhido = jogadores[indice]
            
            # Remove usando o texto exato dele (.remove)
            jogadores.remove(jogador_escolhido)
            print("\nJogador removido com sucesso!")
            
        input("\nPressione Enter para continuar...")
        os.system("cls")
        
    # --- OPÇÃO INVÁLIDA ---
    else:
        print("Opção inválida!")
        input("Pressione Enter para tentar novamente...")
        os.system("cls")