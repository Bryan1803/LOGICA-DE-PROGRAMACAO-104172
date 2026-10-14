import os
os.system("cls")

print("= INSERINDO LIVROS NO VETOR =")
vetor_livro = []

for i in range(5):
    livro = input(f"Digite o nome do {i + 1}º livro: ")
    vetor_livro.append(livro)


print("\n= EXIBINDO LIVROS DO VETOR =")
for i in range(5):
    print(f"Livro {i + 1}: {vetor_livro[i]}")