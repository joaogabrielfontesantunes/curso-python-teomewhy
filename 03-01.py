# Um programa que recebe uma palavra digitada pelo usuário
# e verifica quantas vezes a letra "a" se repete nela.

# %%
count = 0

palavra = input("Escreva uma palavra para descobrir quantas vezes a letra \"a\" se repete nela:").lower()

count = palavra.count("a")

print(f"A palavra \"{palavra}\" tem {count} letra(s) \"a\".")
# %%
