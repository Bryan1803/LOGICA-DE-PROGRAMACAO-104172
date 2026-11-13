import os
os.system("cls")

# Função com retorno e com parâmetro
def verificar_positivo_negativo(numero):
    if numero > 0:
        return f"O número {numero} é Positivo."
    elif numero < 0:
        return f"O número {numero} é Negativo."
    else:
        return "O número é Zero (neutro)."


numero_digitado = int(input("Digite um número: "))

# Chamando a função e guardando o retorno
resultado = verificar_positivo_negativo(numero_digitado)
print(resultado)