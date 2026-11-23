from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: str
    telefone: str
    endereco: str
    
    def mostrar_dados(self):
            print(f"Nome: {self.nome}")
            print(f"Telefone: {self.telefone}")
            print(f"Idade: {self.idade}")
            print(f"Endereço: {self.endereco}")
            print(f"="*30)

    # Função somente para enviar e-mails.
    def nome_e_idade(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"="*30)
        
    def nome_e_telefone(self):
            print(f"Nome: {self.nome}")
            print(f"Telefone: {self.telefone}")
            print(f"="*30)
        
lista_cliente = []
    
print("SOLICITADNO DADOS DE DOIS CLIENTES.")
for i in range(1):
    dados_do_cliente = Cliente(
        nome= input("\nDigite seu nome: "),
        idade= input("Digite sua idade: "),
        telefone= input("Digite seu telefone: "),
        endereco= input("Digite seu endereço: ")
        
    )
    lista_cliente.append(dados_do_cliente)

print("\nEXIBINDO DADOS")
for cliente in lista_cliente:
    print(f"Nome do paciente: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Endereço: {cliente.endereco} ")
    print(f"="*30)
    
    print("\n= EXIBINDO NOME E IDADE =")
for cliente in lista_cliente:
    cliente.nome_e_idade()

print("\n= EXIBINDO NOME E TELEFONE =")
for cliente in lista_cliente:
    cliente.nome_e_telefone()