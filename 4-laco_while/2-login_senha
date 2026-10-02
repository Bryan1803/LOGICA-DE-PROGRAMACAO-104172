import os
import time

os.system("cls")

print("=== TELA DE CADASTRO ===")

while True:
    login_salvo = input("Crie o seu usuário de login: ")
    senha_salva = input("Crie a sua senha de acesso: ")
    
    if login_salvo != "" and senha_salva != "":
        break
    else:
        print("\nO usuário e a senha não podem ficar em branco. Tente de novo.\n")

print("\nCadastro realizado com sucesso.")
print("Redirecionando para a tela de login...")
time.sleep(2)

os.system("cls")

while True:
    print("=== TELA DE ACESSO ===")
    usuario = input("Digite o seu login: ")
    
    if usuario == login_salvo:
        senha = input("Digite a sua senha: ")
        
        if senha == senha_salva:
            print("\nBem-vindo!")
            break
        else:
            print("\nSenha incorreta.")
            input("Pressione Enter para tentar novamente...")
            print("Reiniciando o sistema...")
            time.sleep(1)
            os.system("cls")
    else:
        print("\nUsuário inválido.")
        input("Pressione Enter para tentar novamente...")
        print("Reiniciando o sistema...")
        time.sleep(1)
        os.system("cls")

print("\n= FIM =")