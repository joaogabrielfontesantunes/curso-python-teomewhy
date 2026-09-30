# Um programa que recebe 4 alturas digitadas pelo usuário
# e soma todos os valores para descobrir a altura total.

# %%
alturas = 0

print("Digite 4 alturas para saber a soma delas!")

for _ in range(4):
    alturas += int(input("Digite o valor em centímetros:"))

print(f"A soma das 4 alturas é {alturas}cm.")
# %%
