"""
Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete:
→ Coxinha - R$ 5.00
→ Pastel - R$ 7.00
→ Café - R$ 4.00
→ Suco - R$ 6.00

Faça um algoritmo em que voce seleciona o produto que quer comprar e quantidade. Faça isso até que decida encerrar o programa

Ao final mostre o valor final do pedido a ser pago

"""

print('LANCHONETE')

print('1 → Coxinha R$ 5,00')
print('2 → Pastel R$ 7,00')
print('3 → Café R$ 4,00')
print('4 → Suco R$ 6,00')
print('5 → SAIR')

total = 0
while True:
    op = int(input('Selecione o item desejado: '))
    
    if(op == 1):
        qtd = int(input('Quantidade(unid): '))
        total += qtd * 5.00
        
    elif(op == 2):
        qtd = int(input('Quantidade(unid): '))
        total += qtd * 7.00
        
    elif(op == 3):
        qtd = int(input('Quantidade(unid): '))
        total += qtd * 4.00
        
    elif(op == 4):
        qtd = int(input('Quantidade(unid): '))
        total += qtd * 6.00
        
    elif(op == 5):
        break
    else:
        print('Selecione um produto válido!')

print(f'Total: R$ {total}')