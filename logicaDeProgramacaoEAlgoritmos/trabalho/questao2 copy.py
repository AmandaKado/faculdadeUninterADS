# Constantes
ENFEITE = "*" * 65
PRECOS = {
    "PS": {"P": 30, "M": 45, "G": 60},
    "PD": {"P": 34, "M": 48, "G": 66}
}

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
    while True:
        sabor = input("Escolha o sabor da pizza (PS para Salgada ou PD para Doce): ").upper()
        if sabor in PRECOS:
            return sabor
        print("Sabor inválido. Opções válidas: PS ou PD. Tente novamente.")

# Função para validar tamanho
def validar_tamanho():
    while True:
        tamanho = input("Escolha o tamanho da pizza (P, M ou G): ").upper()
        if tamanho in ["P", "M", "G"]:
            return tamanho
        print("Tamanho inválido. Opções válidas: P, M ou G. Tente novamente.")

# Função principal para realizar o pedido
def realizar_pedido():
    valor_total = 0
    while True:
        # Validação de entradas
        sabor = validar_sabor()
        tamanho = validar_tamanho()

        # Adiciona o preço ao total
        preco = PRECOS[sabor][tamanho]
        valor_total += preco

        # Pergunta se deseja continuar
        while True:
            continuar = input("Deseja pedir mais alguma coisa? [S/N]: ").upper()
            if continuar == "S":
                break  # Sai do loop e permite novo pedido
            elif continuar == "N":
                print(f"O valor total a ser pago é: R$ {valor_total:.2f}")
                return  # Encerra o programa
            else:
                print("Resposta inválida. Responda S para SIM ou N para NÃO.")

# Execução do programa
exibir_menu()
realizar_pedido()
