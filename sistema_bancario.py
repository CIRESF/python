#dados
saldo = 1000
limite_saque_valor = 500
limite_saque = 3
extrato = ""

menu = """---------------------
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
---------------------
R: """

cont = 1

while True:

    n = input(menu)
    
    if n == "1":
        valor = input("Valor de deposito: R$ ") 
        valor = float(valor)   
        if valor>0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("O valor não é válido")
            continue


    elif n== "2": 
        
        if cont <= limite_saque:
            cont += 1
            valor = input("Valor de saque: ")  
            valor = float(valor)

            if valor>0 and valor <= limite_saque_valor and valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
            
            elif valor>0 and valor <= limite_saque_valor and valor > saldo:
                print("Saldo insuficiente")
                continue

            elif valor>0 and valor > limite_saque_valor:
                print("Limite de valor de saque ultrapassado")
                continue

            else:
                print("O valor não é válido")
                continue
        
        else:
                print("Limite de número de saques atingido!")

    elif n == "3":
        print("\n------------Extrato------------")
        print("Não foram efetuados movimentos" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("-------------------------------")

    elif n == "4":
        print("Volte sempre!")   
        break
