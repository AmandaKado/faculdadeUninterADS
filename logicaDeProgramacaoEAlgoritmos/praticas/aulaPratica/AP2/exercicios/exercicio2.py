#Escreva um algoritmo que leia dois valores numericos e que pergunte ao usuário qual operação ele deseja realizar: +, -, * ou /. Exiba na tela o resultado da operação desejada
print('___________________________________________________________________________________________________')
print('CALCULADORA')
print('+')
print('-')
print('*')
print('/')
print('Pressione qualquer outra tecla para sair.')
print('___________________________________________________________________________________________________')

v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))

op = input('Qual operação deseja realizar? ')

if ( op == '+' ):
    resp = v1 + v2
    print(f'Resultado: {v1} + {v2} = {resp}')
elif( op == '-' ):
    resp = v1 - v2
    print(f'Resultado: {v1} - {v2} = {resp}')
elif( op == '*' ):
    resp = v1 * v2
    print(f'Resultado: {v1} x {v2} = {resp}')
elif( op == '/' ):
    resp = v1 / v2
    print(f'Resultado: {v1} / {v2} = {resp}')
else: 
    print('Encerrando programa... ')
