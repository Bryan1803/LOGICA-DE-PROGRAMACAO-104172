from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    telefone: str
    email: str
    
lista_cliente = []

print("SOLICITANDO DADOS DE UM CLIENTE")
for i in range(1):
    dados_do_cliente = Cliente(
        nome= input("\nDigite seu nome: "),
        telefone= input("Digite seu número de telefone: "),
        email= input("Digite seu email: ")
    )
    lista_cliente.append(dados_do_cliente)
    
print("\n= EXIBINDO DADOS =")
for cliente in lista_cliente:
    print(f"Nome: {cliente.nome}")
    print(f"Telefone: {cliente.telefone}")
    print(f"E-mail: {cliente.email}")
    print(f"="*15)