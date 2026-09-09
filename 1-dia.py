import os
os.system("cls")

dia = int(input("Digite dia da semana: "))

match dia:
    case 1:
        print("Final de semana")
    case 2:
        print("Dia útil. ")
    case 3:
        print("Dia útil.")
    case 4:
        print("Dia útil.")
    case 5:
        print("Dia útil.")
    case 6:
        print("Final de semana")
    case _:
        print("Dia inválido.")

        print("=== FIM ===")