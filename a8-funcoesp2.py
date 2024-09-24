def criar_carro(marca, modelo, ano, placa, /, motor, combustivel ):
    print(f"Done! {marca} | {modelo} | {ano} | {placa}")
    print(f"{motor} | {combustivel}")


criar_carro("marca", "modelo", "ano", "placa", combustivel="gasolina", motor="2.0")
criar_carro("marca1", "modelo2", "ano3", "pla-0000", "1.0", "flex")

#criar_carro(placa="placa", modelo="modelo", marca="marca",ano="ano")


print("keywords")
def criar_carro_keyword(*, modelo, ano, placa, marca, motor, combustivel ):
    print(f"Done! {marca} | {modelo} | {ano} | {placa} | {motor} | {combustivel}")
criar_carro_keyword(marca="marca", modelo="modelo", ano="ano", placa="placa", combustivel="gasolina", motor="2.0")



print("keywords and position")
def criar_carro_key_position(modelo, ano, placa,/, *, marca, motor, combustivel ):
    print(f"Done! {marca} | {modelo} | {ano} | {placa} | {motor} | {combustivel}")

criar_carro_key_position("tesla", 2030, "TSL-1000", marca="OPEN", motor="6.0", combustivel="hybrid")


def print_carro_key_position(modelo, ano, placa, /, marca, *, motor, combustivel ):
    print(f"Done! {marca} | {modelo} | {ano} | {placa} | {motor} | {combustivel}")

print_carro_key_position("tesla", 2030, "TSL-1000", marca="OPEN", motor="6.0", combustivel="hybrid")
print_carro_key_position("tesla", 2030, "TSL-1000", "OPEN", motor="6.0", combustivel="hybrid")


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    
    print(f"resultado: {a} {funcao.__name__} {b} = {resultado}")

exibir_resultado(20, 15, somar)
exibir_resultado(20, 15, subtrair)