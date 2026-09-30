# Um programa que verifica se um produto digitado pelo usuário
# já está presente na lista de compras para o churrasco.

# %%
lista_de_compras = ["limão", "farofa", "carvão", "picanha", "guaraná"]

def verificar(produto: str):
    if produto.lower() in lista_de_compras:
        print("Esse produto está na sua lista de compras!")
    else:
        print("Esse produto não está na sua lista de compras!")

verificar(input("Qual produto você vai comprar para o seu churrasco?"))

# %%
