# Um programa que exibe o dobro de um número inserido pelo usuário.

# %%
try:
    numero = float(input("Insira um número para receber o dobro:"))
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro}")
except ValueError:
    print("Digite apenas números!")
# %%
