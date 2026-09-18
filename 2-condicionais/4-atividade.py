import os

# LIMPA O TERMINAL
os.system("cls")

# ENTRADA
nome = (input ("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
serie = (input("Digite sua série: "))
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

# CALCULAR A MÉDIA
media = (primeira_nota + segunda_nota + terceira_nota) / 3

# MÉDIA
print("\n RESULTADO ")
print(f"Média final: {media:.2f}")

# 5. APROVADO OU REPROVADO
if media >= 7:
    
    print("RESULTADO FINAL: APROVADO")
    print("PASSOU DE ANOOOOOOOO! UHULLLL!")
else:
    print("RESULTADO FINAL: REPROVADO")
    print("VC É BURRO PRA KRAIO")