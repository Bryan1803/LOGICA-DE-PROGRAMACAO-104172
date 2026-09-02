import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA.
nome = input("Digite seu nome: ")
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

# PROCESSAMENTO.
IMC= (peso)/altura * altura
if IMC <= 18.5:
    resultado = print(f"{nome} está abaixo do peso ")

elif IMC >= 18.6 and IMC == 24.9:
    resultado = "está no peso ideal (parabéns) "

elif IMC >= 25 and IMC == 29.9:
    resultado = "está levemente acima do peso "

elif IMC >= 30 and IMC == 34.9:
    resultado = "classificado em Obesidade grau I "

elif IMC >= 35.0 and IMC == 39.9:
    resultado = "classificado em Obesidade grau II (severa)"

else:
    IMC > 40
    resultado = "classificado em Obesidade grau III (mórbida) "

# SAÍDA
print("\n= RESULTADO =")
print(f"Resultado: {resultado}")