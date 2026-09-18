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
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

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


# VERIFICANDO SE SÃO IGUAIS
if primeiro_numero == segundo_numero:
    print("Os números são iguais.")
else:
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
