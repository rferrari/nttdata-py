saldo = 500

####
# define function sacar 
def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print("valor sacado: " + str(valor))

    else:
        print(f"Erro: {valor} > saldo")
        #print("Erro: "+str(valor)+" > saldo")

####
# define function deposito  
def deposito(valor):
    global saldo
    saldo += float(valor)
    print(f"Valor {valor} depositado com sucesso")


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