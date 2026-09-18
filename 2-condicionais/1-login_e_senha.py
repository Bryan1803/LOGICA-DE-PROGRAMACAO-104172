import os
os.system("cls")

login = input("Digite seu login: ")
senha = input("Digite sua senha: ") # Removido o int() daqui

# PROCESSAMENTO
login_salvo = "bryan"
senha_salva = "1234"

if login == login_salvo and senha == senha_salva:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos")
