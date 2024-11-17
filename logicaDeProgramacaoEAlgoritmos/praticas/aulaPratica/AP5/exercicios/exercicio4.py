"""
Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas

armazene os dados em um dicionario com listas

ao encerrar o cadastro, apresente:

    total de cadastros
    a media das idades das pessoas
    uma lista de mulheres com menos de 30 anos
    uma lista de homem com a idade acima da media
"""

cadastro = {
    'nome': [],
    'sexo': [],
    'ano' : []
}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N] ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM e N para NÃO!')
        continue

    nome = input('Nome: ')
    sexo = input('Sexo: ')
    ano = input('Ano de nascimento: ')
    
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)