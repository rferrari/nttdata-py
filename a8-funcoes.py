# procedures
def exibir_mensagem(mensagem):
    print("Olá Mundo! " + mensagem)

def exibir_welcome(nome):
    print(f"Olá {nome}!")

def exibir_ola(nome="Aluno"):
    print(f"Olá {nome}!")


exibir_mensagem("my message")
exibir_welcome(nome="MyName")
exibir_ola()

# error
# exibir_mensagem()

# functions
def calcular_total(numeros):
    return (sum(numeros))

def retornar_antecessor_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

print(calcular_total([2,5]))
print(retornar_antecessor_sucessor(5))


def salvar_carro(marca, modelo, ano, placa):
    print(f"Done! {marca} | {modelo} | {ano} | {placa}")


salvar_carro("marca", "modelo", "ano", "placa")

salvar_carro(placa="placa", modelo="modelo", marca="marca",ano="ano")

def exibir_poema(data_extenso, *args, **kwargs):
        texto = "\n".join(args)
        meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
        mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
        print(mensagem)

print()
print()
exibir_poema(
     "Seg, 2024-090-23"
     "Zen Python",
     "Beautifil",
     "Explicit",
     "poem is a poem",
     "poetry is poem",
     "poem is poetry",
     "Explicit Beautifil Beautifil Explicit",
     Author= "Python",
     Ano= "1789"
)
