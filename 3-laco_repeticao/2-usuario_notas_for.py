import os
os.system('cls')

notas = 0

for i in range(3):
    nota = float(input("Digite a nota: ")) 
    notas += nota

media_final = notas / 3
if media_final >= 7:
    resultado = "\nALUNO ESTÁ APROVADO!"

elif media_final >= 4:
    resultado = "\nALUNO ESTÁ EM RECUPERAÇÃO"

else:
    resultado = "\nALUNO ESTÁ REPROVADO"

print(f"\nMédia final: {media_final}")
print(resultado)

print("\nFIM")