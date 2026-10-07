import os
os.system("cls")

soma = 0
contador = 0
resposta = "S"

while True:
        nota = float(input(f"\nDigite a nota: "))
    
        soma += nota
        contador += 1

        resposta = input("Deseja inserir mais uma nota? (S/N): ")
        if resposta == "N":
                break

        media = soma / contador

        print(f"Média: {media:.2f}")
print("= FIM =")