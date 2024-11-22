"""
1-Escreva uma funcao que calcule o fatorial de um numero recebido como parametro e retorne o seu resultado

2-Faca uma validacao dos dados por meio de uma outra funcao, permitidno que somente valores positivos sejam aceitos

3-Crie o help da sua funcao

"""

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input( pergunta))
    return x

def fatorial(num):

    """
    Função que calcula fatorial do número digitado
    """

    fat = 1
    if num == 0:
        return fat
    # Essa parte só execura caso num > 0
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

x = valida_int('Digite o valor para calcular a fatorial: ', 0, 99999)
print(f'{x}! = {fatorial(x)}')

help(fatorial)