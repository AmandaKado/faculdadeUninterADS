"""
Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$100, R$50, R$20, R$10, R$5 e R$1

"""

valor = int(input('Digite um valor para sacar: '))

while True:
    if valor >= 100: 
        cont100 = valor // 100
        valor -= cont100 * 100
        print(f'Cédulas de 100 serão: {cont100}')
        if not valor: 
            break
    if valor >= 50: 
        cont50 = valor // 50
        valor -= cont50 * 50
        print(f'Cédulas de 50 serão: {cont50}')
        if not valor: 
            break
    if valor >= 20: 
        cont20 = valor // 20
        valor -= cont20 * 20
        print(f'Cédulas de 20 serão: {cont20}')
        if not valor: 
            break
    if valor >= 10: 
        cont10 = valor // 10
        valor -= cont10 * 10
        print(f'Cédulas de 10 serão: {cont10}')
        if not valor: 
            break
    if valor >= 5: 
        cont5 = valor // 5
        valor -= cont5 * 5
        print(f'Cédulas de 5 serão: {cont5}')
        if not valor: 
            break
    if valor: 
        cont1 = valor 
        print(f'Cédulas de 1 serão: {cont1}')
        break
    