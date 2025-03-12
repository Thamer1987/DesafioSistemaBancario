

menu = f'''' 
======Menu=====
Escolha uma das opções abaixo:
1 - Depósito.
2 - Saque.
3 - Extrato.
0 - retornar menu.

'''

saldo = 0
limite = 500
saque = saldo
extrato = saldo - saque
numero_saque = 0 
LIMITE_SAQUE = 3


print(menu)




while True:

    opcao = int(input("Digite o numero da opcao: "))

    if opcao == 1:
        valor = float(input("Digite o valor de depósito.\n "))
        if valor > 0:
            saldo += valor
            print(f"Deposito realizado no valor de {valor:.2f}/n")
        else:
            print("Operação invalida!")

    elif opcao == 2:
        valor = float(input("Digite o valor de saque.\n "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        saque = valor - saldo
        if excedeu_saldo:
            print("Operação invalida! Saldo insuficiente")
        elif excedeu_limite:
            print("Operação invalida! Valor de saque excedido")
        elif excedeu_saque:
            print("Operação invalida! Excedeu numero de saques permitido")
        elif valor <= saldo:
            print(f"Saque no valor de {valor:.2f} realizado com sucesso.\n")
        else:
            print("Operação invalida!")
        
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {extrato:.2f}")
        print("==========================================")
    elif opcao == 0:
        break
    else:
        print(f"""Opção invalida! Retorne ao menu principal""")
    





