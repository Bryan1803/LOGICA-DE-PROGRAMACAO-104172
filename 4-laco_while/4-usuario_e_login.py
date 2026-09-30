import os
import time

# Limpa a tela antes de começar tudo
os.system("cls")

LOGIN_CORRETO = "admin"
SENHA_CORRETA = "1234"

while True:
    print("=== TELA DE ACESSO ===")
    usuario = input("Digite o seu login: ")
    
    # 1. Testamos se o login está correto
    if usuario == LOGIN_CORRETO:
        senha = input("Digite a sua senha: ")
        
        # 2. Testamos se a senha está correta
        if senha == SENHA_CORRETA:
            print("\nAcesso permitido! Bem-vindo ao sistema.")
            break
        else:
            print("\nSenha incorreta!")
            input("Pressione Enter para tentar novamente...")
            print("Reiniciando o sistema...")
            time.sleep(1)  # Espera 1 segundo antes de limpar
            os.system("cls")
            
    # 3. Se o login estiver errado, cai direto aqui no else
    else:
        print("\nUsuário inválido!")
        input("Pressione Enter para tentar novamente...")
        print("Reiniciando o sistema...")
        time.sleep(1)  # Espera 1 segundo antes de limpar
        os.system("cls")

print("\n= FIM =")