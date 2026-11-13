import os
os.system("cls")

# Função com retorno
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

print("= SOLICITANDO DADOS =")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Usando a função com parâmetros e
# inserindo o retorno na variável soma.
media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)

print("\n= EXIBINDO DADOS =")
print(f"\nMédia: {media}")
print(f"\nResultado: {situacao}")