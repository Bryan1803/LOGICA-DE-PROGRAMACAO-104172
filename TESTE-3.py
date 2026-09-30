import os
os.system("cls")

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura (ex: 1.75): "))

while True:
    genero = input("Digite o gênero (M para Masculino / F para Feminino): ").upper().strip()
    
    if genero == "M" or genero == "F":
        break
    else:
        print("\nGênero inválido! Tente novamente.")

if genero == "M":
    peso_ideal = (72.7 * altura) - 58
    genero_texto = "Masculino"
else:
    peso_ideal = (62.1 * altura) - 44.7
    genero_texto = "Feminino"

print("\n=== RESULTADO ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Gênero: {genero_texto}")
print(f"Altura: {altura:.2f}m")
print(f"O peso ideal estimado é: {peso_ideal:.2f} kg")

print("\n= FIM =")
