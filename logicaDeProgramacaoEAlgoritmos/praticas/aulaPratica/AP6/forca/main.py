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

if not fH.existeArquivo(arquivo):
    fH.criarArquivo(arquivo)

while True:
    mostrar_menu()
    try:
        opcao = int(input("Escolha a opção (1/2/3): "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número [1, 2, 3].")
        continue

    if opcao == 1:
        print("Iniciar jogo!")
        j.jogar()
    elif opcao == 2:
        print("Score: ")
        dados = fH.listarArquivo(arquivo)
        if not dados:
            print("Score vazio")
        else:
            for i, jogador in enumerate(dados, start=1):
                if len(jogador) >= 2:
                    print(f"{i} → {jogador[0]}, Pontuação: {jogador[1]}")
    elif opcao == 3:
        print("Saindo do jogo... Até mais")
        break
    else:
        print("Opção inválida. Tente uma das opções [1/2/3]")
