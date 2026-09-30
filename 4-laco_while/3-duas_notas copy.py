import os
os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(2):
    while True:
        nota = float(input(f"\nDigite a {i+1}ª nota entre 0 e 10: "))

        if nota < 0 or nota > 10:
            print("\nNota inválida, tente novamente!")
        else:
            soma = soma + nota
            break

media = soma / QUANTIDADE_NOTAS

print(f"\nMédia: {media:.2f}")
print("= FIM =")