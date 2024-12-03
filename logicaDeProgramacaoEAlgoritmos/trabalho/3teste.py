def exibir_desenvolvedor():
    # Exibe o nome do desenvolvedor e o nome da empresa
    print("\nBem-vindos a Madeireira da Lenhadora Amanda Mayumi Kado\n")

def escolha_tipo():
    # Função para selecionar o tipo de madeira
    tipos = {
        "PIN": 150.40,
        "PER": 170.20,
        "MOG": 190.90,
        "IPE": 210.10,
        "IMB": 220.70
    }
    while True:
        print("\nTipos de madeira disponíveis:")
        print("→ Tora de Pinho (PIN)")
        print("→ Tora de Peroba (PER)")
        print("→ Tora de Mogno (MOG)")
        print("→ Tora de Ipê (IPE)")
        print("→ Tora de Imbuia (IMB)")
        escolha = input("Envie somente a sigla do tipo de madeira: ").strip().upper()
        if escolha in tipos:
            return tipos[escolha]  # Retorna o valor correspondente ao tipo escolhido
        else:
            print("\nInsira um tipo de madeira válido!")

def qtd_toras():
    # Função para obter a quantidade de toras e calcular o desconto
    while True:
        try:
            qtd = float(input("Quantidade de toras (em m³): "))
            if qtd > 2000:
                print("Não é aceito pedidos acima de 2000 m³!\n")
            elif qtd >= 1000:
                return qtd, 16 / 100
            elif qtd >= 500:
                return qtd, 9 / 100
            elif qtd >= 100:
                return qtd, 4 / 100
            elif qtd > 0:
                return qtd, 0 / 100
            else:
                print("Quantidade inválida. Tente novamente.\n")
        except ValueError:
            print("Valor inserido não é numérico! Tente novamente.\n")

def transporte():
    # Função para selecionar o tipo de transporte
    opcoes = {
        1: 1000,
        2: 2000,
        3: 2500
    }
    while True:
        print("\nOpções de transporte:")
        print("1 - Rodoviário (R$ 1000)")
        print("2 - Ferroviário (R$ 2000)")
        print("3 - Hidroviário (R$ 2500)")
        try:
            escolha = int(input("Escolha o tipo de transporte (1/2/3): "))
            if escolha in opcoes:
                return opcoes[escolha]
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Insira um número válido (1, 2 ou 3).\n")

# Código principal
exibir_desenvolvedor()

# Escolher tipo de madeira
preco_madeira = escolha_tipo()

# Obter quantidade de toras e desconto
quantidade, desconto = qtd_toras()

# Escolher transporte
valor_transporte = transporte()

# Calcular total a pagar
subtotal = preco_madeira * quantidade
valor_com_desconto = subtotal * (1 - desconto)
total = valor_com_desconto + valor_transporte

# Exibir detalhes do pedido
print("\nResumo do Pedido:")
print(f"→ Preço por m³: R$ {preco_madeira:.2f}")
print(f"→ Quantidade de toras: {quantidade} m³")
print(f"→ Desconto aplicado: {desconto * 100:.0f}%")
print(f"→ Subtotal: R$ {subtotal:.2f}")
print(f"→ Valor com desconto: R$ {valor_com_desconto:.2f}")
print(f"→ Transporte: R$ {valor_transporte:.2f}")
print(f"→ Total a pagar: R$ {total:.2f}")
