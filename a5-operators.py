number1 = 10
number2 = 20
number3 = 5

print(number1 - number2 * number3)
print(number1 - number2)
print(number1 / number2)
print(number1 // number2)
print(number1 * number3)

print((number1 - number2) * number3)
print(number1 - (number2 * number3))

x = (number3**2)
print(x)

x = (number3**3)
y = (number1 + number2)

print(x, y, sep=" <> ", end="!\n")


x = (number3 % 3)
y = (number1 % number2)

print(x, y, sep=" <> ", end="!\n")
