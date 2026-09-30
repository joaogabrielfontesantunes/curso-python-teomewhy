# Um programa que exibe uma história de forma pausada, parágrafo por parágrafo.
# A cada parágrafo, o leitor deve apertar Enter para avançar ao próximo,
# e a tela é limpa entre cada um para manter a leitura limpa e focada.
# Ao final, uma mensagem de encerramento é exibida.

# %%
import os

historia = """Era uma vez, um aventureiro que gostava de tesouros
Certo dia, ele encontrou uma caverna e decidiu explorar ela
Tudo estava escuro, mas por sorte, ele tinha uma lanterna de bolso
No interior da caverna, encontrou um baú com muito ouro
Ele foi para casa alegre e viveu feliz com seu tesouro"""

paragrafos_historia = historia.split("\n")

print("Ao ler a história, aperte \"Enter\" para continuar")
for i in range(len(paragrafos_historia)):
    print(f"[{i+1}/5]", paragrafos_historia[i])
    while input() != "":
        print("Tecle apenas \"Enter\"")
        pass
    os.system("cls" if os.name == "nt" else "clear")
print("A história acabou! Espero que tenha gostado")
# %%
