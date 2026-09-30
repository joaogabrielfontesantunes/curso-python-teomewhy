# Um programa que recebe um número inteiro, valida a entrada,
# verifica se ele possui raiz quadrada exata e exibe o resultado.

# %%
import math

def verificar_raiz(numero: int) -> None:
    raiz = math.sqrt(numero)
    if raiz.is_integer():
        print(f"Raiz exata: {int(raiz)}")
    else:
        print("Não tem raiz exata")

try:
    numero = int(input("Digite um número para receber a sua raiz quadrada:"))
    verificar_raiz(numero)
except ValueError:
    print("Digite apenas números inteiros!")
# %%
