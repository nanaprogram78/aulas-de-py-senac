menu = """
[d]depositar
[s]sacar
[e]extrato
[q]sair
=>
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informa o valor do deposito: "))

        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}/n"

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu__limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você nao tem saldo suficiente")
        elif excedeu__limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif excedeu_saques:
            print("Operação falhou! Numero máximo de saques excedido")   
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}/n" 
            numero_saques += 1
        else:
            print("operção falhou!O valor informado é invalido")
    elif opcao == "e":
        print("/n =========== EXTRATO ============")
        print("Não foram realizadas movimentaçõoes." if not extrato else extrato)
        print(f"/n Saldo: R$ {saldo:.2f}")
        print("=========================")

    elif opcao == "q":
        break

