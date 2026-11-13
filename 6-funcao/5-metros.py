import os
os.system("cls")

# Função com retorno e com parâmetro
def metros_para_centimetros(metros):
    return metros * 100


print("= SOLICITANDO DADOS =")
metros = float(input("Digite o valor em metros: "))

centimetros = metros_para_centimetros(metros)

print("\n= EXIBINDO DADOS =")
print(f"{metros} metros correspondem a {centimetros} centímetros.")
