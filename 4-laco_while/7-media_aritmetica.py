import os
os.system("cls")

soma_notas = 0
quantidade_validas = 0
contador = 0

total_notas = int(input("Quantas notas deseja digitar no total?: "))

while contador < total_notas:
    nota = float(input("Digite a nota: "))
    
    if nota < 0 or nota > 10 or nota % 1 > 0:
        break
        
    soma_notas = soma_notas + nota
    quantidade_validas = quantidade_validas + 1
    contador = contador + 1

media = soma_notas / quantidade_validas
print(media)