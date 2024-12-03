def exibir_desenvolvedor():
    print("\nBem-vindos a Madeireira da Lenhadora Amanda Mayumi Kado\n")

def escolha_tipo():
    # Dicionário com preços das madeiras
    tipos = {
        "PIN": 150.40,
        "PER": 170.20,
        "MOG": 190.90,
        "IPE": 210.10,
        "IMB": 220.70
    }
    
    # Solicita o tipo de madeira até que o usuário escolha uma opção válida
    while True:
        print("\nEntre com o tipo de madeira desejado:")
        print("\nPIN → Tora de Pinho")
        print("PER → Tora de Peroba")
        print("MOG → Tora de Mogno")
        print("IPE → Tora de Ipê")
        print("IMB → Tora de Imbuia\n")
        escolha = input(">> ").strip().upper()

        if escolha in tipos:
            return tipos[escolha]  # Retorna o preço da madeira escolhida
        else:
            print("\nEscolha inválida, entre com o modelo novamente!")

def qtd_toras():
    # Solicita a quantidade de toras e aplica o desconto baseado na quantidade
    while True:
        try:
            qtd = float(input("Entre com a quantidade de toras (m³): "))
            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras!\nPor favor entre com a quantidade novamente.\n")
            elif qtd >= 1000:
                return qtd, 16 / 100 # Desconto de 16% para quantidades >= 1000
            elif qtd >= 500:
                return qtd, 9 / 100 # Desconto de 9% para quantidades >= 500
            elif qtd >= 100:
                return qtd, 4 / 100 # Desconto de 4% para quantidades >= 100
            elif qtd > 0:
                return qtd, 0 / 100 # Sem desconto para quantidades < 100
            else:
                print("Quantidade inválida. Tente novamente.\n")
        except ValueError:
            print("Valor inserido não é numérico! Tente novamente.\n")

def transporte():
    # Dicionário com preços dos tipos de transporte
    opcoes = {
        1: 1000,
        2: 2000,
        3: 2500
    }
    
    # Solicita a escolha do tipo de transporte até que seja válida
    while True:
        print("\nEscolha o tipo de Transporte: ")
        print("\n1 → Rodoviário - R$ 1000")
        print("2 → Ferroviário - R$ 2000")
        print("3 → Hidroviário - R$ 2500\n")
        try:
            escolha = int(input(">>  "))
            if escolha in opcoes:
                return opcoes[escolha] # Retorna o valor do transporte escolhido
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Insira um número válido (1, 2 ou 3).\n")

# Código principal:

# Chama função de exibir nome do desenvolvedor
exibir_desenvolvedor()

# Chama as funções para escolher tipo de madeira, quantidade de toras e tipo de transporte
preco_madeira = escolha_tipo()
quantidade, desconto = qtd_toras()
valor_transporte = transporte()

# Calcula o total a pagar considerando preço da madeira, desconto e valor do transporte
subtotal = preco_madeira * quantidade
valor_com_desconto = subtotal * (1 - desconto)
total = valor_com_desconto + valor_transporte

# Exibe total
print(f"→ Total a pagar: R$ {total:.2f}")
