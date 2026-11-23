from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int
    altura: float
    
lista_clientes = []
    
print("SOLICITADNO DADOS DE DOIS CLIENTES.")
for i in range(2):
    dados_do_cliente = Cliente(
        nome= input("\nDigite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        altura= float(input("Digite sua altura: "))
    )
    lista_clientes.append(dados_do_cliente)

print("\nEXIBINDO DADOS")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Float: {cliente.altura}")
    print(f"="*15)