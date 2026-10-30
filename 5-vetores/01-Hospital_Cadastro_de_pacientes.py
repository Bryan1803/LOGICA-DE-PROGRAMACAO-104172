import os
os.system("cls")

pacientes = []

while True:
    print('''
    == MERCADINHO BIG BOM ==
    
    1. Cadastrar paciente
    2. Listar pacientes
    3. Atualizar paciente
    4. Excluir paciente
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
        print("=== CADASTRAR PACIENTE ===")
        
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        
        # Junta o nome e o sobrenome em uma palavra só
        nome_completo = nome + " " + sobrenome
        
        # Coloca o texto na lista usando o append
        pacientes.append(nome_completo)
        
        print("Paciente cadastrado!")
        input("Pressione Enter para continuar...")
        os.system("cls")
        
    # --- 2. LISTAR ---
    elif opcao == "2":
        os.system("cls")
        print("=== LISTA DE PACIENTES ===")
        
        if len(pacientes) == 0:
            print("Não há pacientes cadastrados.")
        else:
            # Mostra cada nome da lista com o número na frente
            for i in range(len(pacientes)):
                print(f"{i + 1}. {pacientes[i]}")
                
        input("Pressione Enter para continuar...")
        os.system("cls")
        
    # --- 3. ATUALIZAR ---
    elif opcao == "3":
        os.system("cls")
        print("=== ATUALIZAR PACIENTE ===")
        
        if len(pacientes) == 0:
            print("Não há pacientes para atualizar.")
        else:
            for i in range(len(pacientes)):
                print(f"{i + 1}. {pacientes[i]}")
                
            numero = int(input("Digite o número do paciente que quer alterar: "))
            indice = numero - 1
            
            novo_nome = input("Digite o novo nome: ")
            novo_sobrenome = input("Digite o novo sobrenome: ")
            
            # Substitui o texto antigo pelo novo texto
            pacientes[indice] = novo_nome + " " + novo_sobrenome
            
            print("Paciente atualizado!")
            
        input("Pressione Enter para continuar...")
        os.system("cls")
        
    # --- 4. EXCLUIR ---
    elif opcao == "4":
        os.system("cls")
        print("=== EXCLUIR PACIENTE ===")
        
        if len(pacientes) == 0:
            print("Não há pacientes para excluir.")
        else:
            for i in range(len(pacientes)):
                print(f"{i + 1}. {pacientes[i]}")
                
            numero = int(input("Digite o número do paciente que quer remover: "))
            indice = numero - 1
            
            # Pegamos o texto do paciente que escolhemos deletar
            paciente_escolhido = pacientes[indice]
            
            # Remove usando o nome exato dele: .remove("Nome Sobrenome")
            pacientes.remove(paciente_escolhido)
            
            print("Paciente excluído!")
            
        input("Pressione Enter para continuar...")
        os.system("cls")
        
    # --- OPÇÃO ERRADA ---
    else:
        print("Opção inválida!")
        input("Pressione Enter para tentar novamente...")
        os.system("cls")