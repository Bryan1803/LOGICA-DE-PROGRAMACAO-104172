from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class Clientes:
    nome: str
    email: str
    telefone: int
    endereco: str
    
QUANTIDADE_CLIENTES = 2

lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    novo_cliente = Clientes(
        nome=input("Digite seu nome: "),
        email=input("Digite seu e-mail: "),
        telefone=int(input("Digite seu telefone: ")),
        endereco=input("Digite seu endereço: ")
    )
    lista_clientes.append(novo_cliente)

# Salvando no arquivo
arquivo = "fornecedor.csv"
with open(arquivo, "a", encoding="utf-8") as arquivo_clientes:
    for cliente in lista_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}\n")
        
print("Clientes salvos com sucesso!")