saldo = 1000
limite = 100
#contaEspecial = True
contaEspecial = False

while saldo > 0:
    print("Seu Saldo é: " + str(saldo))
    if(contaEspecial != True):
        print("Seu Limite é: " + str(limite))

    saque = input("Deseja sacar quanto? ")
    try:
        saque = float(saque)
    except ValueError:
        print("enter valid number")
        continue

    if ((saldo >= saque) and (saque <= limite)) or (contaEspecial and saldo >= saque):
        saldo = int(saldo) - saque
    else:
        print("Error: Seu saldo é: " + str(saldo))
        print("Error: Seu limite é: " + str(limite))
        print("Error: Conta especial: " + str(contaEspecial))

print("Acabou seu dinheiro :(")
