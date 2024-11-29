ENFEITE = "*" * 65 

# Função para exibir o menu
def exibir_menu():
    print("\n")
    print(ENFEITE)
    print("-" * 10 + " Bem-vindos à Pizzaria da Amanda Mayumi Kado " + "-" * 10)
    print(ENFEITE)
    print("-" * 28 + " CARDÁPIO " + "-" * 27)
    print(ENFEITE)
    print("----|   Tamanho  |  Pizza Salgada (PS)  |  Pizza Doce (PD)  |----")
    print("----|      P     |  R$ 30.00            |  R$ 34.00         |----")
    print("----|      M     |  R$ 45.00            |  R$ 48.00         |----")
    print("----|      G     |  R$ 60.00            |  R$ 66.00         |----")
    print(ENFEITE)
    print("\n")
# Função para validar o sabor
def validar_sabor():
    while True:
        sabor = input("Escolha o sabor (PS para Salgada ou PD para Doce): ").upper()
        if sabor in ["PS", "PD"]:
            return sabor
        print("Sabor inválido. Tente novamente.\n")
        continue

# Função para validar o tamanho
def validar_tamanho():
    while True:
        tamanho = input("Escolha o tamanho (P, M ou G): ").upper()
        if tamanho in ["P", "M", "G"]:
            return tamanho
        print("Tamanho inválido. Tente novamente.\n")
        continue

# Função para calcular o preço
def calcular_preco(sabor, tamanho):
    if sabor == "PS":
        if tamanho == "P":
            return 30
        elif tamanho == "M":
            return 45
        elif tamanho == "G":
            return 60
    elif sabor == "PD":
        if tamanho == "P":
            return 34
        elif tamanho == "M":
            return 48
        elif tamanho == "G":
            return 66
    return 0

# Função principal para realizar o pedido
def realizar_pedido():
    valor_total = 0
    while True:
        sabor = validar_sabor()
        tamanho = validar_tamanho()
        preco = calcular_preco(sabor, tamanho)
        
        valor_total += preco
        
        if sabor == "PS":
            print(f"Você pediu uma Pizza salgada, tamanho {tamanho}: R$ {preco:.2f}.\n")
        else:
            print(f"Você pediu uma Pizza doce, tamanho {tamanho}: R$ {preco:.2f}.\n")

        while True:
            continuar = input("Deseja pedir mais alguma coisa? [S/N]: ").upper()
            if continuar == "S":
                break
            elif continuar == "N":
                print(f"\nTotal a pagar: R$ {valor_total:.2f}\n")
                return
            else:
                print("Resposta inválida. Responda S ou N.\n")
                continue

# Execução do programa
exibir_menu()
realizar_pedido()
