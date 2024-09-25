opcao = -1

while True: 
    if(opcao == -1):
        while opcao != 0:
            try:
                opcao = int(input("[1] Sacar   [2] Extrato   [0] Sair  "))
                if opcao == 1:
                    print("opcao 1")
                elif opcao == 2:
                    print("opcao 2")
                else:
                    print("Obrigado")
            except ValueError:
                 continue
    
    opcao = (input("Realmente quer sair? Y/N"))
    if(opcao.upper() == "Y"):
        break
    else:
         opcao = -1


