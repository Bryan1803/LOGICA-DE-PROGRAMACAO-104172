import os
os.system("cls")

def limpar():
    os.system("cls")


def cadastrar_senha():
    while True:
        limpar()
        print("=== BANCO COFRINHO · CADASTRO ===\n")
        nova_senha = input("\nCrie uma senha para sua conta: ")
        if nova_senha == "":
            print("\nA senha não pode ficar vazia.\n")
            input("\nPressione Enter para continuar...")
        else:
            confirmar = input("\nConfirme a senha criada: ")
            if nova_senha == confirmar:
                print("\nSenha cadastrada com sucesso!\n")
                input("\nPressione Enter para continuar...")
                return nova_senha
            else:
                print("\nAs senhas não coincidem. Tente novamente.\n")
                input("\nPressione Enter para continuar...")


def verificar_senha(senha_cadastrada):
    tentativas = 0

    while tentativas < 3:
        limpar()
        print("=== BANCO COFRINHO · ACESSO ===\n")
        senha = input("\nDigite sua senha: ")

        if senha == senha_cadastrada:
            return "liberado"
        else:
            tentativas = tentativas + 1
            restantes = 3 - tentativas
            print(f"\nSenha incorreta! Tentativas restantes: {restantes}\n")
            input("\nPressione Enter para continuar...")

    print("\nAcesso bloqueado por excesso de tentativas.\n")
    return "bloqueado"


def menu():
    print("=== BANCO COFRINHO · CAIXA ===\n")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("0 - Sair\n")


def ver_saldo(saldo):
    print(f"\nSaldo: R$ {saldo:.2f}\n")


def depositar(saldo, extrato):
    valor = float(input("\nValor do depósito: R$ "))
    if valor >= 0.01:
        saldo = saldo + valor
        extrato.append(f"\nDepósito: R$ {valor:.2f}")
        print("\nDepósito realizado!\n")
    else:
        print("\nValor inválido.\n")
    return saldo


def sacar(saldo, extrato):
    valor = float(input("\nValor do saque: R$ "))
    if valor < 0.01:
        print("\nValor inválido.\n")
    elif valor > 1000:
        print("\nLimite máximo por saque é de R$ 1.000,00.\n")
    elif valor > saldo:
        print("\nSaldo insuficiente.\n")
    else:
        saldo = saldo - valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("\nSaque realizado!\n")
    return saldo


def ver_extrato(extrato, saldo, qtd_depositos, qtd_saques):
    print("\n=== EXTRATO ===\n")
    if extrato == []:
        print("Nenhuma movimentação.\n")
    else:
        for item in extrato:
            print(item)
        print()
    print(f"\nTotal de depósitos: {qtd_depositos}")
    print(f"Total de saques: {qtd_saques}\n")
    print(f"Saldo atual: R$ {saldo:.2f}\n")


def sair():
    print("\nObrigado por usar o Banco Cofrinho! Até logo.\n")


saldo = 500.0
extrato = []
qtd_depositos = 0
qtd_saques = 0

senha_cadastrada = cadastrar_senha()

if verificar_senha(senha_cadastrada) == "liberado":
    while True:
        limpar()
        menu()
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                ver_saldo(saldo)
            case "2":
                saldo_antes = saldo
                saldo = depositar(saldo, extrato)
                if saldo > saldo_antes:
                    qtd_depositos = qtd_depositos + 1
            case "3":
                saldo_antes = saldo
                saldo = sacar(saldo, extrato)
                if saldo < saldo_antes:
                    qtd_saques = qtd_saques + 1
            case "4":
                ver_extrato(extrato, saldo, qtd_depositos, qtd_saques)
            case "0":
                sair()
                break
            case _:
                print("\nOpção inválida!\n")

        input("\nPressione Enter para continuar...")