import os
os.system("cls")

nome = input("Digite seu nome: ")
registro = input("Digite o seu sexo de registro: ")
ano = int(input("Digite seu ano de nascimento: "))
print("\nMINÍMO 18 ANOS")

# PROCESSAMENTO

if registro == "masculino" and ano <= 2008:
    print("Se apresente para o serviço militar obrigatório")
else:
    print("Não deve apresentar-se")