print('Olá mundo um', end="   ")
print('Olá mundo dois')

def soma(x = 0, y = 0, z = 0):
    """
    Explicação do funcionamento da função:
    
    A função retorna o somatório de até 3 valores numéricos quaisquer. Todos os parâmetros são opcionais.
    """
    return x + y + z

print(soma(2, 4))
help(soma)