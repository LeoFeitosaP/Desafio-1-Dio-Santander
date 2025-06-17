menu = """
---------Bem-vindo ao Banco Santander!---------
Selecione uma opção:

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Digite o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor inválido! O depósito deve ser um valor positivo.")

    elif opcao == "S":
        valor = float(input("Digite o valor a ser sacado: R$ "))
        if numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido! Você já realizou {numero_saques} saques.")
        elif valor > saldo:
            print("Saldo inssuficiente para realizar o saque!")
        elif valor > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f}!")
       
        else:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

    elif opcao == "E":
        print("Extrato")
        if not extrato:
            print("Nenhum movimento encontrado.")
        else:
            print("Movimentos:")
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "Q":
        print("Obrigado por utilizar nossos serviços!")
        break  
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")
        continue
