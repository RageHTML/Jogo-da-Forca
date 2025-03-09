import random
from collections import Counter

# Palavras disponíveis para o jogo da forca
palavras_disponiveis = '''mecanico droga sexo cigarro rothmans skate deyvid carro casa passaro'''

# Escolher uma das palavras disponíveis
selecionar_palavras = palavras_disponiveis.split(' ')  # Corrigido o delimitador
palavra = random.choice(selecionar_palavras)

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