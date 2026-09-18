import os
os.system("cls")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
caracter = input("Digite um dos caracteres para o cálculo (+, -, * ou /) : ")

resultado = float

match caracter:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        resultado = numero1 / numero2

print(f"Número 1 informado : {numero1}")
print(f"Número 2 informado : {numero2}")
print(f"Sinal de operação informado : {caracter}")

print("\n-- RESULTADO -- ")
print(f"Resultado: {resultado}")
