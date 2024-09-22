for numero in range(1,21):
    if ((numero <= 10) or (numero >10 and numero in [15, 16, 20])):
        print(f"#tabuada do {numero}")
        for valor in range(0, (numero*10+1), numero): 
            print(valor, end=" ")
        print("\n")
else:
    print("bons estudos")


# print("#tabuada do 5")
# for numero in range(0, 51, 5):
#       print(numero, end=" ")
# else:
#       print("\n\n")

