# Um programa que simula uma venda de água, onde o usuário escolhe
# o tipo de garrafa e a quantidade, valida as entradas e exibe o total a pagar.

# %%

try:
    agua = int(input("""Eu vendo garrafas d'água. Digite o número correspondente ao tipo requerido.
                1. Água Natural - R$1,5
                2. Água Com Gás - R$2,5"""))

    if agua not in [1, 2]:
        print("Opção inválida!")
    else:
        quantidade = int(input("Quantas garrafas você gostaria de comprar?"))
        if quantidade <= 0:
            print("Quantidade inválida!")
        else:
            preco = 1.5 if agua == 1 else 2.5
            total = preco * quantidade
        print(f"Você pagará R${total}")
except ValueError:
    print("Digite apenas números!")
# %%
