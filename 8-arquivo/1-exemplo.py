from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Clientes:
    nome: str
    idade: int
    altura: float
    
QUATIDADE_CLIENTES = 2

lista_clientes = []

for i in range(QUATIDADE_CLIENTES):
    novo_cliente = Clientes(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        altura= float(input("Digite sua altura: ")),
    )
    lista_clientes.append(novo_cliente)
    
    #Salvando um arquivo
    arquivo = "dados_clientes.csv"
    with open(arquivo, "a") as arquivo_clientes:
        for cliente in lista_clientes:
            arquivo_clientes.write(f"{cliente.nome}, {cliente.idade}, {cliente.altura}\n")
            
    print("Cliente salvo com sucesso!")