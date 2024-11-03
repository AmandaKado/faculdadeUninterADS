#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

kmPercorrido = int(input('Quantidade de km percorridos pelo carro alugado: '))
diasAlugado = int(input('O carro foi alugado por quantos dias? '))

custoDiario = diasAlugado * 60
custoKmRodado = kmPercorrido * 0.15
precoTotal = custoDiario + custoKmRodado

print(precoTotal)