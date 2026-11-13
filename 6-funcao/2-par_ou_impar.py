import os
os.system("cls")

# Função sem retorno e com parâmetro
def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} éímpar.")
    return resultado


numero = int(input("Digite um número: "))

resultado = verificar_par_impar

print("\n= EXIBINDO DADOS =")
print(f"O número: {numero} é par")
print(f"O número: {numero} é ímpar")