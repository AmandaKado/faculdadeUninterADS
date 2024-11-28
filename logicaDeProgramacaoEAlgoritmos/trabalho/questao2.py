"""

QUESTÃO 2 de 4 - Conteúdo até aula 04

Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma Pizzaria que vende sabores de Pizzas Doces e Pizzas Salgadas. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.

A Loja possui seguinte relação:

     Tamanho P: Pizza Salgada (PS) custa 30 reais e a Pizza Doce (PD) custa 34 reais;
     Tamanho M: Pizza Salgada (PS) custa 45 reais e a Pizza Doce (PD) custa 48 reais;
     Tamanho G: Pizza Salgada (PS) custa 60 reais e a Pizza Doce (PD) custa 66 reais;

Elabore um programa em Python que:

    A. Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
    
        Por exemplo: print(“Bem-vindos a Pizzaria do Bruno Kostiuk”)
        Além do seu nome completo, deve-se implementar um print com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];
    
    B. Deve-se implementar o input do sabor (PS/PD) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de PS e PD [EXIGÊNCIA DE CÓDIGO 2 de 8];
    
    C. Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
    
    D. Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
    
    E. Deve-se implementar um acumulador para somar os valores dos pedidos (valor total do pedido) [EXIGÊNCIA DE CÓDIGO 5 de 8];
    
    F. Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
    
    G. Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
    
    H. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
    
    I. Deve-se apresentar na saída de console uma mensagem com o seu nome completo e o menu para o cliente conhecer as opções [EXIGÊNCIA DE SAÍDA
    DE CONSOLE 1 de 4];
    
    J. Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
    
    K. Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
    
    L. Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]; 

"""
# Variável criada para montar menu da pizzaria:
enfeite = "*" * 65 
print(enfeite)
#  Mostra quem desenvolveu o Sistema:
print("-" * 10 + " Bem-vindos a Pizzaria da Amanda Mayumi Kado " + "-" * 10) 
print(enfeite)
# Mostra no console o menu para o cliente:
print("-" * 28 + " CARDÁPIO " + "-" * 27) 
print(enfeite)
print("----|   Tamanho  |  Pizza Salgada (PS)  |  Pizza doce (PD)  |----")
print("----|      P     |  R$ 30.00            |  R$ 34.00         |----")
print("----|      M     |  R$ 45.00            |  R$ 48.00         |----")
print("----|      G     |  R$ 60.00            |  R$ 66.00         |----")
print(enfeite)

# Variável acumuladora para somar o total do pedido:
valorTotal = 0

while True:
    # Variável para armazenar o sabor escolhido
    while True:  # Loop para garantir uma entrada válida
        sabor = input("Escolha o sabor da pizza (PS para Salgada ou PD para Doce): ").upper() # Função upper para garantir que mesmo que o usuário insira caractere minusculo seja considerado
        if sabor in ["PS", "PD"]:  # Verifica se o sabor está entre os válidos
            break  # Sai do loop se o sabor for válido
        else:
            print("Sabor inválido. Tente novamente.")  # Informa o erro e continua no loop

    # Variável para armazenar o tamanho escolhido
    while True:  # Loop para garantir uma entrada válida
        tamanho = input("Escolha o tamanho da pizza (P, M ou G): ").upper()
        if tamanho in ["P", "M", "G"]:  # Verifica se o tamanho está entre os válidos
            break  # Sai do loop se o tamanho for válido
        else:
            print("Tamanho inválido. Tente novamente.")  # Informa o erro e continua no loop

    if sabor == "PS": # Se o sabor escolhido for salgado, verifica os tamanhos e precifica
        if tamanho == "P":
            preco = 30
        elif tamanho == "M":
            preco = 45
        else:
            preco = 60
    else: # Se o sabor escolhido for doce, verifica os tamanhos e precifica
        if tamanho == "P":
            preco = 34
        elif tamanho == "M":
            preco = 48
        else:
            preco = 66
            
    valorTotal += preco

    continuar = input("Deseja pedir mais alguma coisa? [S/N]")
    
    if (continuar == "N"):
        print("")