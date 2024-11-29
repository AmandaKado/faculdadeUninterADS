# Váriaveis constantes
ENFEITE = "*" * 65

# Função para exibir o menu
def exibir_menu():
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

# Função para validar sabor
def validar_sabor():
    while True:  # Repetição para entrada válida
        sabor = input("Escolha o sabor da pizza (PS para Salgada ou PD para Doce): ").upper()
        if sabor in ["PS", "PD"]:
            return sabor
        print("Sabor inválido. Opções válidas: PS ou PD. Tente novamente.")
        continue  # Reinicia o loop em caso de erro

# Função para validar tamanho
def validar_tamanho():
    while True:  # Repetição para entrada válida
        tamanho = input("Escolha o tamanho da pizza (P, M ou G): ").upper()
        if tamanho in ["P", "M", "G"]:
            return tamanho
        print("Tamanho inválido. Opções válidas: P, M ou G. Tente novamente.")
        continue  # Reinicia o loop em caso de erro

# Função para calcular o preço com if/elif/else aninhados
def calcular_preco(sabor, tamanho):
    if sabor == "PS":  # Pizza Salgada
        if tamanho == "P":
            return 30
        elif tamanho == "M":
            return 45
        elif tamanho == "G":
            return 60
    elif sabor == "PD":  # Pizza Doce
        if tamanho == "P":
            return 34
        elif tamanho == "M":
            return 48
        elif tamanho == "G":
            return 66
    else:
        return 0  # Caso de erro (não deveria ocorrer devido à validação anterior)

# Função principal para realizar o pedido
def realizar_pedido():
    valor_total = 0
    while True:  # Loop principal para novos pedidos
        # Validação de entradas
        sabor = validar_sabor()
        tamanho = validar_tamanho()

        # Calcula o preço com if/elif/else aninhados
        preco = calcular_preco(sabor, tamanho)
        valor_total += preco
        print(f"Você adicionou uma pizza {sabor} tamanho {tamanho} por R$ {preco:.2f}.")
        print(f"Total parcial: R$ {valor_total:.2f}")

        # Pergunta se deseja continuar
        while True:  # Loop para validar a resposta
            continuar = input("Deseja pedir mais alguma coisa? [S/N]: ").upper()
            if continuar == "S":
                print("Continuando com o pedido...")
                break  # Sai do loop de validação e retorna ao início do pedido
            elif continuar == "N":
                print(f"O valor total a ser pago é: R$ {valor_total:.2f}")
                print("Finalizando o pedido. Obrigado por comprar na Pizzaria da Amanda!")
                return  # Encerra a função principal e o programa
            else:
                print("Resposta inválida. Responda S para SIM ou N para NÃO.")
                continue  # Reinicia o loop em caso de resposta inválida

# Execução do programa
exibir_menu()
realizar_pedido()
