import os
os.system("cls")

def logo_senai():
    print("================================")
    print("         SENAI - BAHIA          ")
    print("================================")

def mostrar_dados(nome, email, telefone):
    print("\n--- DADOS CADASTRADOS ---")
    print(f"Nome:     {nome}")
    print(f"E-mail:   {email}")
    print(f"Telefone: {telefone}")
    print("-------------------------")

logo_senai()

print("\nPor favor, insira os dados solicitados:")
logo_senai()
nome = input("\nDigite o nome: ")
logo_senai()
email = input("\nDigite o e-mail: ")
logo_senai()
telefone = input("\nDigite o telefone: ")

logo_senai()
mostrar_dados(nome, email, telefone)