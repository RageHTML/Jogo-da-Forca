import random  # Usamos random para escolher de forma aleatória as palavras disponíveis.
from collections import Counter
import tkinter as tk
from tkinter import messagebox


# A variável (palavras_disponiveis) disponibiliza diversas palavras da área de TI para serem selecionadas.
# 1 - A alteração das palavras é muito fácil, mas precisam seguir um padrão.
# 2 - Coloque as palavras uma abaixo da outra e usem (''' ''') - sem as chaves: "()"
# 3 - Não coloque vírgulas, não é necessário.

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
Protocolo
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
Versionamento
'''

# Organizar as palavras_disponiveis em uma lista:
# 1 - O método splitlines() retorna uma lista das palavras selecionadas separadas e organizadas.

organizar_em_lista = palavras_disponiveis.splitlines()

# Escolher a palavra principal:
# 1 - Define uma variável "palavra"
# 2 - Usa o método random e a variável choice para escolher uma palavra da nossa lista de palavras.
# 3 - Ele é especialmente útil para garantir que certas partes do código só sejam executadas quando o script é rodado diretamente

palavra = random.choice(organizar_em_lista)

# Configurações iniciais do jogo
letra_corretas = ""
chances = len(palavra) + 2  # Quantidade de letras da palavra + 2 chances extras

# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("600x400")  # Largura x Altura

# Label para exibir a palavra oculta
label_palavra = tk.Label(janela, text="", font=("Arial", 24))
label_palavra.pack(pady=20)

# Entry para o jogador inserir uma letra
entry_letra = tk.Entry(janela, font=("Arial", 18))
entry_letra.pack(pady=10)

# Botão para enviar o palpite
botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 14))
botao_enviar.pack(pady=10)

# Label para mostrar as chances restantes
label_chances = tk.Label(janela, text="", font=("Arial", 14))
label_chances.pack(pady=10)

# Função para atualizar a interface
def atualizar_interface():
    # Atualiza a palavra oculta
    palavra_oculta = " ".join([letra if letra in letra_corretas else "_" for letra in palavra])
    label_palavra.config(text=palavra_oculta)

    # Atualiza as chances restantes
    label_chances.config(text=f"Chances restantes: {chances}")

# Função para processar o palpite
def processar_palpite():
    global chances, letra_corretas

    # Obter a letra digitada pelo jogador
    advinhar = entry_letra.get().lower()
    entry_letra.delete(0, tk.END)  # Limpar o campo de entrada

    # Validação do palpite
    if not advinhar.isalpha():  # O método isalpha() retorna True se todos os caracteres da string forem letras, e False caso contrário.
        messagebox.showwarning("Entrada inválida", "Digite apenas letras!")
        return
    elif len(advinhar) != 1:  # Usamos o método len() para contar a quantidade de caracteres da palavra que foram inseridos no terminal. Garante que o usuário insira apenas uma letra por vez.
        messagebox.showwarning("Entrada inválida", "Digite apenas 1 letra!")
        return
    elif advinhar in letra_corretas:
        messagebox.showwarning("Letra repetida", "Você já tentou essa letra!")
        return

    # Verificar se a letra está na palavra
    if advinhar in palavra:
        letra_corretas += advinhar  # Adicionar a letra às letras descobertas
        messagebox.showinfo("Letra correta!", "Você acertou uma letra!")
    else:
        chances -= 1
        messagebox.showerror("Letra incorreta!", "Essa letra não está na palavra.")

    # Atualizar a interface
    atualizar_interface()

    # Verificar se o jogador ganhou ou perdeu
    if Counter(letra_corretas) == Counter(palavra):
        messagebox.showinfo("Parabéns!", f"Você ganhou! A palavra era: {palavra}")
        janela.quit()
    elif chances == 0:
        messagebox.showerror("Fim de jogo", f"Você perdeu! A palavra era: {palavra}")
        janela.quit()

# Vincular o botão à função
botao_enviar.config(command=processar_palpite)

# Atualizar a interface inicial
atualizar_interface()

# Iniciar o loop principal da interface
janela.mainloop()