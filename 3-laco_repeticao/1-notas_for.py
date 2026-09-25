import os
os.system('cls')

notas = 0

for i in range(4):
    nota = float(input("Digite a nota: ")) 
    notas += nota

media_final = notas / 4

print(f"\nMédia final: {media_final}")
print("\nFIM")
