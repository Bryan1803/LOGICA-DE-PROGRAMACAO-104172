import os
os.system("cls")

print("= INSERINDO LIVROS NO VETOR =")
vetor_livro = []

for i in range(5):
    livro = input(f"Digite o nome do {i + 1}º livro: ")
    vetor_livro.append(livro)


print("\n= EXIBINDO LIVROS DO VETOR =")
for indice, livro in enumerate(vetor_livro, start=1):
    print(f"{indice}º: {livro}")