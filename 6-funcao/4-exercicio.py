import os
os.system("cls")

def logo_senai():
    print('\n==================')
    print('  SENAI - BAHIA   ')
    print('==================')

def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone: ")
    return nome, email, telefone

def mostrar_dados(nome, email, telefone):
    print("\n--- DADOS DO CLIENTE ---")
    print(f'Nome: {nome}')
    print(f'E-mail: {email}')
    print(f'Telefone: {telefone}')

nome = ""
email = ""
telefone = ""

while True:
    logo_senai()
    print("1 - CADASTRAR CLIENTE")
    print("2 - MOSTRAR DADOS DO CLIENTE")
    print("3 - SAIR")
    
    opcao = input("\nEscolha uma opção: ")
    
    match opcao:
        case "1":
            nome, email, telefone = cadastrar_cliente()
        case "2":
            if nome == "":
                print("\nNenhum cliente cadastrado ainda!")
            else:
                mostrar_dados(nome, email, telefone)
        case "3":
            print("\nSaindo do programa...")
            exit()
        case _:
            print("\nOpção incorreta!")