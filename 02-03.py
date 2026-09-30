# Um programa que verifica se o sobrenome digitado pelo usuário
# pertence à família Santos, à família Silva, às duas, ou a nenhuma.

# %%
def verificar(nome: str):
    tem_santos = "santos" in nome.lower()
    tem_silva = "silva" in nome.lower()

    if tem_santos and tem_silva:
        print("Você é da família Santos e da família Silva!")
    elif tem_santos:
        print("Você é da família Santos!")
    elif tem_silva:
        print("Você é da família Silva!")
    else:
        print("Você não é da família Santos ou da família Silva")
    
verificar(input("Qual o seu nome?"))

# %%
