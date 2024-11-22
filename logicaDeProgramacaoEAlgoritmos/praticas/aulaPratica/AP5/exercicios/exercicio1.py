"""
Data uma lista contendo as notas de alunos em uma disciplina, escreva uma expressao para:

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

a) encontrar quantos alunos tiraram nota 7

b) alterar a ultima nota para 4

c) encontrar a maior nota

d) ordenar a lista de notas

e) a media das notas

"""

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] # Lista de numeros

print(notas.count(7)) # conta quantos 7 tem nessa lista

notas[-1] = 4 # transforma o ultimo item da lista em 4
print(notas) 

print(max(notas)) # pega o maior numero da lista

notas.sort() # Ordena a lista em ordem crescente
print(notas) 

print(sum(notas) / len(notas)) # calcula a media dos numeros

