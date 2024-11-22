"""
    Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maças, laranjas ou bananas. Deverá ser apresentado, na tela, um menu com a opção 1 para maça, 2 para laranja e 3 para banana

    Depois de escolhida a fruta, deve-se digitar quantas unidade se quer comprar. O algoritmo deve calcular o preço total a pagar pelo produto escolhido e mostrá-lo na tela. 

    Considere que uma maça custa R$ 2,30; uma laranja, R$ 3,60; e uma banana, R$ 1,85

"""
print("Feirinha do Brás")
print("/n")
print("1 - Maçã")
print("2 - Laranja")
print("3 - Banana")

produto = int(input("Qual sua escolha? "))
qtd = int(input("Quantas unidade? "))

match (produto):
    case 1:
        pagar = qtd * 2.3
        print(f"Você comprou {qtd} maças. Total à pagar: {pagar}")
    case 2:
        pagar = qtd * 3.6
        print(f"Você comprou {qtd} laranjas. Total à pagar: {pagar}")
    case 3:
        pagar = qtd * 1.85
        print(f"Você comprou {qtd} bananas. Total à pagar: {pagar}")
    case _:
        print("Produto inválido! ")