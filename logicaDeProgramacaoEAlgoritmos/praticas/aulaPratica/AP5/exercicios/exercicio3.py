import random

def Valida_int(pergunta, min, max):
    """Valida se o número está entre min e max."""
    x = int(input(pergunta))
    while x < min or x > max:
        print(f"Digite um valor entre {min} e {max}.")
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    """Determina o vencedor da rodada."""
    global v1, v2, empate
    if jogador1 == jogador2:
        empate += 1
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
        v1 += 1
    else:
        v2 += 1
    return [v1, v2, empate]

# Programa principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Sair')

jogadas = []
resultados = []
v1 = 0
v2 = 0 
empate = 0

while True: 
    j1 = Valida_int('Escolha sua jogada: ', 0, 3)
    if j1 == 0:
        break
    j2 = random.randint(1, 3)
    jogadas.append((j1, j2))
    resultados = vencedor(j1, j2)
    
print("\nResultado das rodadas:")
for index, jogada in enumerate(jogadas):
    print(f"Rodada {index + 1}: Jogador 1 escolheu {jogada[0]}, Computador escolheu {jogada[1]}")

print(f'\nNúmeros de vitórias do jogador 1: {resultados[0]}')
print(f'Números de vitórias do computador: {resultados[1]}')
print(f'Números de empates: {resultados[2]}')
