import fileHandler as fH
import desenhos as d
from random import choice

def jogar():
    lista_palavras = []
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    if not arquivo:
        print("Erro: O arquivo de palavras não foi encontrado ou está vazio.")
        return
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)
    arquivo.close()

    if not lista_palavras:
        print("Erro: Nenhuma palavra encontrada no arquivo.")
        return

    palavra_sorteada = choice(lista_palavras)

    for _ in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input("Quem está jogando? ")

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # Condição de vitória
        if adivinha == palavra_sorteada:
            print("Você acertou!!!")
            break

        # Tentativa do jogador
        tentativa = input("\nDigite uma letra: ").lower().strip()
        if tentativa in digitadas:
            print("Você já usou essa letra! ")
            continue

        digitadas.append(tentativa)
        if tentativa in palavra_sorteada:
            acertos.append(tentativa)
        else:
            erros += 1
            print("Errou!")

        score = d.desenhar_forca(erros)

        # Condição de derrota
        if erros == 6:
            print(f"Você perdeu! A palavra era {palavra_sorteada}")
            break

    fH.inserir_dados('score.txt', nome, score)

