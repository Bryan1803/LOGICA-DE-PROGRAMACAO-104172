import os
os.system("cls")

def limpar():
    os.system("cls")


def mostrar_menu():
    print("=== BANCO COFRINHO · CAIXA ===\n")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("0 - Sair\n")


def mostrar_saldo(saldo):
    print(f"\nSaldo: R$ {saldo:.2f}\n")


def depositar(saldo, extrato):
    valor = float(input("\nValor do depósito: R$ "))
    if valor >= 0.01:
        saldo = saldo + valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("\nDepósito realizado!\n")
    else:
        print("\nValor inválido.\n")
    return saldo


def sacar(saldo, extrato):
    valor = float(input("\nValor do saque: R$ "))
    if valor < 0.01:
        print("\nValor inválido.\n")
    elif valor > saldo:
        print("\nSaldo insuficiente.\n")
    else:
        saldo = saldo - valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("\nSaque realizado!\n")
    return saldo


def mostrar_extrato(extrato, saldo):
    print("\n=== EXTRATO ===\n")
    if extrato == []:
        print("Nenhuma movimentação.\n")
    else:
        for item in extrato:
            print(item)
        print()
    print(f"Saldo atual: R$ {saldo:.2f}\n")


def sair():
    print("\nObrigado por usar o Banco Cofrinho! Até logo.\n")


saldo = 500.0
extrato = []

while True:
    limpar()
    menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            ver_saldo(saldo)
        case "2":
            saldo = depositar(saldo, extrato)
        case "3":
            saldo = sacar(saldo, extrato)
        case "4":
            ver_extrato(extrato, saldo)
        case "0":
            sair()
            break
        case _:
            print("\nOpção inválida!\n")

    input("\nPressione Enter para continuar...")