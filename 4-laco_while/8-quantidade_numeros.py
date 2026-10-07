import os
os.system("cls")

quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0
quantidade_geral = 0
contador = 0

while contador < 5:
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero == 0:
        break
        
    if numero >= 100:
        break
        
    if numero % 2 == 0:
        quantidade_pares = quantidade_pares + 1
        soma_pares = soma_pares + numero
    else:
        quantidade_impares = quantidade_impares + 1
        
    soma_geral = soma_geral + numero
    quantidade_geral = quantidade_geral + 1
    contador = contador + 1

print("\n=== RESULTADOS ===")
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)

if quantidade_geral > 0:
    if quantidade_pares > 0:
        media_pares = soma_pares / quantidade_pares
        print("Média dos valores pares:", media_pares)
    else: 
        print("Média dos valores pares: 0")
        
    media_geral = soma_geral / quantidade_geral
    print("Média geral dos números:", media_geral)
else:
    print("Média dos valores pares: 0")
    print("Média geral dos números: 0")
