import os
os.system("cls")

# Funções com retorno e com parâmetros
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Não é possível dividir por zero."
    else:
        resultado = n1 / n2
        return f"{resultado:.2f}"

print("= SOLICITANDO DADOS =")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n= EXIBINDO DADOS =")
print(f"\nSoma: {somar(num1, num2):.2f}")
print(f"\nSubtração: {subtrair(num1, num2):.2f}")
print(f"\nMultiplicação: {multiplicar(num1, num2):.2f}")
print(f"\nDivisão: {divisao(num1, num2)}")
