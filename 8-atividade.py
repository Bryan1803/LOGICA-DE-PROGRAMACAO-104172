import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA
primeiro_numero = int(input ("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

#PROCESSAMENTO
soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = primeiro_numero
    menor = segundo_numero

# SAÍDA
print(f"\nMédia: {media}")
print(f"\nSoma: {soma}")
print(f"\nProduto: {produto}")
print(f"\nMaior: {maior}")
print(f"\nMenor: {menor}")