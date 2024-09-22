saldo = 500
saldo = 2500
saldo = 90

#contaEspecial = True
contaEspecial = False 
contaUniversitaria = False


####
# define function sacar 
def sacar(valor):
    global saldo
    if contaEspecial:
        if saldo >= valor:
            saldo -= valor
            print("valor sacado: " + str(valor))
            operacao = True
        else:
            print(f"Erro: {valor} > saldo")
            #print("Erro: "+str(valor)+" > saldo")
            operacao = False
    elif contaUniversitaria:
        if saldo >= valor:
            saldo -= valor
            print("valor sacado: " + str(valor))
            operacao = True
        else:
            print(f"Erro: {valor} > saldo")
            operacao = False
            #print("Erro: "+str(valor)+" > saldo")
    else:
        operacao = False
        print("entre em contato com seu gerente")

    status = "Sucesso" if operacao else "Falha"
    print(f"{status} ao realizar o saque!")

####
# define function deposito  
def deposito(valor):
    global saldo
    saldo += float(valor)
    print(f"Valor {valor} depositado com sucesso")


# estrutura condiconal
if saldo < 100:
    print("Saldo baixo")
elif saldo > 500:
    print("Quer comprar seguro?")
else:
    print("Bom dia!")

#### main

print("Seu Saldo eh: " + str(saldo))

sacar(100)
print("Seu Saldo eh: " + str(saldo))
sacar(1000)
print("Seu Saldo eh: " + str(saldo))

deposito(250)
print("Seu Saldo eh: " + str(saldo))

sacar(750)
print("Seu Saldo eh: " + str(saldo))

sacar(650)
print("Seu Saldo eh: " + str(saldo))
