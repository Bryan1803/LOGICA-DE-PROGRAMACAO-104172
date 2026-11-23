from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    telefone: str
    email: str
    
    # Função dentro da classe
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"="*30)

lista_cliente = []

print("= SOLICITANDO DADOS =")
for i in range(2):
    dados = Cliente(
        nome= input("\nDigite seu nome: "),
        telefone= input("Digite seu número de telefone: "),
        email= input("Digite seu email: ")
    )
    lista_cliente.append(dados)
    
print("\n= EXIBINDO DADOS =")
for cliente in lista_cliente:
    cliente.mostrar_dados()