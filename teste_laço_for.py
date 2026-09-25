import os
os.system('cls')

notas = 0
recuperacao = 0

for i in range(3):
    nota = float(input("Digite a nota: ")) 
    notas += nota

media_final = notas / 3
if media_final >= 7:
    print("\nALUNO ESTÁ APROVADO!")

elif media_final >= 4:
    print("\nALUNO ESTÁ EM RECUPERAÇÃO")

print(f"\nO aluno tirou: {recuperacao} na recuperação")

if recuperacao > 7:
    print("\nO ALUNO ESTÁ APROVADO PELA RECUPERAÇÃO")

else:
    print("\n O ALUNO NÃO FOI APROVADO PELA RECUPERAÇÃO")

print(f"\nMédia final: {media_final}")
print("\nFIM")