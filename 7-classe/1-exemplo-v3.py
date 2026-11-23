from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int
    
lista_clientes = []
    
# SOLICITADNO DADOS DE UM CLIENTE
lista_clientes.append(Cliente(nome="Marta", idade=30))
lista_clientes.append(Cliente(idade=40, nome="José"))

for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"="*15)