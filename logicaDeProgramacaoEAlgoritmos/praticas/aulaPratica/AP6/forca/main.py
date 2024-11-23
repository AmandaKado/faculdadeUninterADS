"""
    Criar um jogo da forca, contendo as opçoes:
    
    1. JOGAR
    2. SCORE
    3. SAIR
    
    Para o JOGAR, o jogador deverá adivinhar a palavra que será carregada de uma lista de palavras dentro de um arquivo de texto
    
    Ao jogar, o nome do jogador deve ser perguntado
    
    Este nome será armazenado no final da jogada, junto com o score que o jogador fez
    
    O nome e o score devem ser armazenados dentro de um arquivo
    
    Na opção de SCORE, mantenha salva a lista de jogadores e seus respectivos scores
    
    Mostre os scores na tela quando selecionar essa opçao
"""

import jogo as j
import fileHandler as fH

def mostrar_menu():
    print("=" * 30)
    print(" " * 7 + "JOGO DA FORCA")
    print("=" * 30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR\n")
    print("=" * 30)
    
    print("\nDICA: Nome de uma fruta")

arquivo = 'score.txt'

if fH.existeArquivo(arquivo):
    print("Arquivo foi localizado no computador!")
else:
    print("Arquivo não existe!")
    fH.criaArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input("Escolha a opção (1/2/3):"))
    
    if opcao == 1:
        print("Iniciar jogo! ")
        j.jogar()
    elif opcao == 2:
        print("Score: ")
        dados = fH.listarArquivo("score.txt")
        if not dados:
            print("Score vazio")
        else:
            i = 1
            for jogador in dados:
                print(f"{i} → {jogador[0]}, Pontuação: {jogador[1][:-1]}")
                i += 1
    elif opcao == 3:
        print("Saindo do jogo... Até mais")
        break
    else:
        print("Opção inválida. Tente uma das opções [1/2/3]")