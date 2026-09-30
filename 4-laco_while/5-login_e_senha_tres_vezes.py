import os
import time
os.system("cls")

tentativas = 0
login_salvo = "admin"
senha_salva = "1234"

for i in range(3):
    tentativas += 1
    if tentativas <= 3:
        print(f"Tentativa: {tentativas}")
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    
    if login == login_salvo and senha == senha_salva:
            print("\nBem-vindo!")
    else:
            print("\nLogin ou senha inválido!")
            print("Tente novamente! \n")
            input("Pressione uma tecla para continuar...")
            os.system("cls")
            
else:
    print("= FIM =")
