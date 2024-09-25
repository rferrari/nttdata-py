NAME = "product"

print(NAME)

price = 10.30
print("price = 10.30")
print(price)


print("price = price /2")
price = price /2
print(price)

print("price = price * 7.8")
price = price * 7.8
print(price)
print(int(price))

print("price // 2 price / 2")
print(price // 2)
print(int(price // 2))
print(price / 2)

result = f"product {NAME} {price}"
print(result)

result = f"product {NAME} {price//2}"
print(result)

result = f"product {NAME} {int(price//2)}"
print(result)

result = f"product {NAME} {str(price/2)}"
print(result)

result = type(price/2)
print(result)

result = type(price//2)
print(price//2)
print(result)

result = type(int(price))
print(result)

result = type(NAME)
print(result)
