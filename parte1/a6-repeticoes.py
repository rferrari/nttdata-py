texto = input("informe um texto:")
VOGAIS = ["A", "E", "I", "O",  "U"]

for letra in texto:
    if letra.upper() in VOGAIS:
            print(letra, end="")
else:
      print()
      print("Executa else Final for loop")


for numero in range(0,11):
      print(numero, end="\n")
