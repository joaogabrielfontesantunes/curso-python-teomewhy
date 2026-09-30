# Um programa que recebe valores digitados pelo usuário
# e soma todos eles para calcular o saldo total.

# %%
saldo = 0

while True:
    valor = input("Digite um valor para ser processado em seu saldo:")
    if valor == "":
        break

    saldo += float(valor)

print(f"O seu saldo total é: {saldo}")
# %%
