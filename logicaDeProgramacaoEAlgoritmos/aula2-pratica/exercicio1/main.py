#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto
precoProduto = float(input('Qual o preço do produto?'))
percentualDesconto = float(input('Qual o percentual do desconto?'))
valorDesconto =  precoProduto  * (percentualDesconto / 100)
valorFinalProduto = precoProduto - valorDesconto

print(f'Você vai ter um desconto de R${valorDesconto}, ficando só R${valorFinalProduto}')