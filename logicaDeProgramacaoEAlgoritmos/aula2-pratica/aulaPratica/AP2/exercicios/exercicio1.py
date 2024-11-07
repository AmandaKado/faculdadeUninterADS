
# Faça um algoritmo que receba tres valores, representando os lados de um triangulo fornecidos pelo usuário. Verifique se os valores formam um triangulo e classifique como
# equilátero tres lados iguais
# isosceles dois lados iguais
# escaleno tres lados diferentes

print('Digite o tamanho de cada lado do triangulo!')

a = int(input('Tamanho do lado A: '))
b = int(input('Tamanho do lado B: '))
c = int(input('Tamanho do lado C: '))

if(( a > 0 and b > 0 and c > 0) and ( a + b > c and b + c > a and c + a > b )): #verifica se é um triangulo
    print('Isso não é um triängulo!')
    if( a !=  b and a != c and b != c):
        print('Esse triangulo é escaleno')
    else:
        if( a == b and b == c ):
            print('Esse triangulo é equilatero')
        else:
            print('Esse triangulo é isosceles')
else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo')