# Um programa que simula a venda de um sorvete, com opções de tipo,
# sabor e cobertura.

# %%
sorvete = {
    "tipos": {1: 1.0, 2: 2.5, 3: 4.0},
    "sabores": {1: "morango", 2: "creme", 3: "chocolate"},
    "coberturas": {1: 1.5, 2: 1.5, 3: 1.5, 4: 0}
}

def escolher(mensagem: str, opcoes: list) -> int:
    escolha = int(input(mensagem))
    if escolha not in opcoes:
        raise ValueError("Opção inválida!")
    return escolha

try:
    tipo = escolher("""Eu vendo sorvetes. Digite o número correspondente ao tipo requerido.
                1. Casquinha - R$1,0
                2. Cascão - R$2,5
                3. Cestinha - R$4,0""", [1, 2, 3])
    sabor = escolher("""Escolha o sabor do sorvete.
                          1. Morango
                          2. Creme
                          3. Chocolate""", [1, 2, 3])
    cobertura = escolher("""Escolha a cobertura do sorvete.
                                  1. Caramelo - R$1,5
                                  2. Morango - R$1,5
                                  3. Chocolate - R$1,5
                                  4. Sem cobertura - R$0,0""", [1, 2, 3, 4])
    
    valor = sorvete["tipos"][tipo] + sorvete["coberturas"][cobertura]
    print(f"Seu sorvete de {sorvete["sabores"][sabor]} custará R${valor}")
except ValueError:
    print("Digite apenas números!")
# %%
