#Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string digitada. Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string

palavra = input('Digite um texto: ')

meioIndice = int(len(palavra)/2)
print(meioIndice)

metade = (palavra[0:meioIndice])
print(metade)

print(metade[1-meioIndice:meioIndice])
