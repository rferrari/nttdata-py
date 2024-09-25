saldo = 1000
limite = 100
#contaEspecial = True
contaEspecial = False

yesResponsesList = ["S", "s", "sim", "Sim"]
noResponsesList = ["N", "n", "Não", "Nao", "nao", "não"]
validResponses = yesResponsesList + noResponsesList

print(saldo is limite)
print(saldo is not limite)

app_name = "App Caixa Banco"
print("Caixa in app_name")
print("Caixa" in app_name)

lista_agencias = ["ag001", "ag409", "ag200"]
print(lista_agencias)

print("ag001 in lista_agencias")
print("ag001" in lista_agencias)

print("ag200 not in lista_agencias")
print("ag200" not in lista_agencias)

print("ag000 in lista_agencias")
print("ag000" in lista_agencias)


while saldo > 0:
    print("\n\n")
    welcomeMessage = "Bem Vindo Cliente"
    if(contaEspecial):
        welcomeMessage += " Especial"
    
    print(welcomeMessage)
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
        if(saque > saldo):
            print("Error: saldo >= saque: " + str(saldo))
        if((not contaEspecial) and (saque >= limite)):
            print("Error: Seu limite de saque é: " + str(limite))

            queroContaEspecial = ""
            while (queroContaEspecial not in validResponses):
                queroContaEspecial = input("Deseja ser cliente especial pagando apenas 10? [S/N]")
            
            if(queroContaEspecial in yesResponsesList):
                saldo -= 10
                contaEspecial = True

        if(contaEspecial):
            print("Conta especial: Sem Limites Saque ")

print("Acabou seu dinheiro :(")
