import os

# Limpa o terminal
os.system("cls")

# 1. ENTRADA DE DADOS
genero = input("Selecione o seu gênero (M ou F): ").upper()
altura = float(input("Digite sua altura : "))

peso_ideal = 0.0
match genero:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        print("Gênero inválido! Use apenas M ou F.")
        exit()

# 3.SAÍDA
print("\n=== RESULTADO ===")
print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
