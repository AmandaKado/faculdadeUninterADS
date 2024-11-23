import fileHandler as fH
import desenhos as d
from random import choice

def jogar():
    lista_palavra = list()
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)
    
palavra_sorteada = choice(lista_palavras)

for i in range(50):
    print()

digitadas = []
acertos = []
erros = 0

nome = input("Quem está jogando? ")

while True:
    adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
    
    #CONDICAO DE VITORIA
    if adivinha == palavra_sorteada:
        print("Você acertou!!!")
        break
    #TENTATIVAS
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já usou essa letra! ")
        continue
    else:
        digitadas += tentativa # ou append
        if tentativa in palavra_sorteada:
            acertos += tentativa
        else:
            erros += 1
            print("Errou burro!!")
    # CONDICAO FIM DE JOGO
    if erros == 6: 
        print(f"Perdeu otário, podre! A palavra era {palavra_sorteada}")
        break