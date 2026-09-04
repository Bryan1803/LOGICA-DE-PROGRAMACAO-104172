import os
os.system("cls")

nota = float(input("Digite sua nota: "))

print("\nCRITÉRIOS PARA A NOTA SER MOSTRADA É: ")
print("\nNOTA PRECISA ESTAR ENTRE 0 E 10")

if nota <= 10 and nota >= 0:
    print(f"\nA NOTA É: {nota}")

else:
    print("\nERRO. A NOTA DEVE SER ENTRE 0 E 10")