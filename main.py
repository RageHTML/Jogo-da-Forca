import random # usamos random para escolher de forma aleatoria as palavras disponíveis.
from tabulate import tabulate
from collections import Counter



# A váriavel (palavras_disponivel) disponibiliza diversas palavras da área de TI para serem selecionada apenas uma.
# 1 - A alteraçaõ das palavras é muito fácil, mas precisam seguir um padrão. 
# 2 - Coloque as palavras uma abaixo da outra e usem ('''  ''') - sem as chaves: "()"
# 3 - Não coloque vírgulas não é necessário.

palavras_disponiveis = '''
Software
Internet 
Rede Servidor
Nuvem
Banco de dados
Algoritmo
Programação
Código
Framework
Interface
Usabilidade
Sistema
Aplicativo
Desenvolvedor
Debug
Compilador
Script
Linguagem
Python
JavaScript
HTML
CSS
Backend
Frontend
API
Prtocolo
Firewall
Segurança
Backup
Cache
Domínio
Hospedagem
Virtualização
Container
DevOps
Inteligência Artificial
Machine Learning
Big Data
IoT 
Blockchain
Criptografia
Autenticação
Responsivo
Open Source
Kernel
Terminal
Pipeline
Versionamento  # <- altere aqui se quiser adicionar mais palavras.
'''

# Organizar as palavras_disponiveis em uma lista:
# 1 - O método spitlines() retorna uma lista das palavras selecionadas separadas e organizadas, esse método é muito útil para processar e manipular textos em Python!. 

organizar_em_lista = palavras_disponiveis.splitlines() 

# Como saber as respostas e ganhar o jogo de forma fácil:
# 1 - tire a "#" para ativar, coloque a "#" para desativar.
# 2 - agora todas as palavras vão aparecer no seu terminal.

print(tabulate(palavras_disponiveis, headers=["Palavras"], tablefmt="grid")) 

# Agora que as palavras estão organizadas em listas, vamos selecionar a palagvra principal do nosso jogo.
# usamos random 
palavra = random.choice(organizar_em_lista) 

if __name__ == '__main__':
    print("Descubra a palavra!")

    # Exibir os espaços vazios para cada letra da palavra
    for _ in palavra:
        print('_', end=' ')
    print()

    jogando = True
    letras_descobertas = ""  # Lista para armazenar as letras adivinhadas pelo jogador
    chances = len(palavra) + 2  # Quantidade de letras da palavra + 2 chances extras

    while chances > 0:
        print()
        print(f"Chances restantes: {chances}")
        try:
            advinhar = input("Digite uma letra para adivinhar: ").lower()  # Converter para minúscula
        except KeyboardInterrupt:
            print("\nTchau, tente novamente!")
            exit()

        # Validação do palpite
        if not advinhar.isalpha():
            print("Digite apenas letras!")
            continue
        elif len(advinhar) != 1:
            print("Digite apenas 1 letra!")
            continue
        elif advinhar in letras_descobertas:
            print("Você já tentou essa letra!")
            continue

        # Verificar se a letra está na palavra
        if advinhar in palavra:
            letras_descobertas += advinhar  # Adicionar a letra às letras descobertas
            print("Letra correta!")
        else:
            print("Letra incorreta!")
            chances -= 1

        # Exibir o estado atual da palavra
        for char in palavra:
            if char in letras_descobertas:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        # Verificar se o jogador ganhou
        if Counter(letras_descobertas) == Counter(palavra):
            print("\nParabéns, você ganhou! A palavra era:", palavra)
            break

    # Se o jogador perdeu
    if chances == 0:
        print("\nVocê perdeu! A palavra correta era:", palavra)