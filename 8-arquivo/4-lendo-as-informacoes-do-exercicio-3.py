from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Clientes:
    nome: str
    email: str
    telefone: int
    endereco: str

lista_clientes = []
    
#Lendo um arquivo
arquivo = "fornecedor.csv"
with open(arquivo, "r") as arquivo_clientes:
    for linha in arquivo_clientes:
        nome, email, telefone, endereco = linha.strip().split(",")
        lista_clientes.append(Clientes(
            nome=nome, email=str(email), telefone=int(telefone), endereco=str(endereco)
        ))
            
print("\nExibindo dados dos clientes: ")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Endereço: {cliente.endereco}")
    print("==========================")