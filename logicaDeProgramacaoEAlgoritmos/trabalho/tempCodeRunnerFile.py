def exibir_desenvolvedor():
    print("\nSistema desenvolvido por Amanda Mayumi Kado\n")

# Função para validar entrada numérica
def validar_numero(prompt, tipo = float, min_valor = 0):
    while True:
        try:
            valor = tipo(input(prompt))
            if valor < min_valor:
                print(f"Por favor, insira um valor maior ou igual a {min_valor}.")
            else:
                return valor
        # except para garantir que será inserido um número
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")

# Função para calcular o valor mensal do plano
def calcular_valor_mensal(valor_base, idade):
    if idade >= 0 and idade < 19:
        porcentagem = 100 / 100  # 100%
    elif idade >= 19 and idade < 29:
        porcentagem = 150 / 100  # 150%
    elif idade >= 29 and idade < 39:
        porcentagem = 225 / 100  # 225%
    elif idade >= 39 and idade < 49:
        porcentagem = 240 / 100  # 240%
    elif idade >= 49 and idade < 59:
        porcentagem = 350 / 100  # 350%
    elif idade >= 59:
        porcentagem = 600 / 100  # 600%
    else:
        return None  # Idade inválida

    # Cálculo do valor mensal
    return valor_base * porcentagem

# Função principal para execução do programa
def main():
    exibir_desenvolvedor()

    # Entrada dos dados
    valor_base = validar_numero("Insira o valor base do plano: ", float, 0)
    idade = validar_numero("Idade do cliente: ", int, 0)

    # Cálculo do valor mensal
    valor_mensal = calcular_valor_mensal(valor_base, idade)

    if valor_mensal is not None:
        print(f"O valor mensal do plano é de: R$ {valor_mensal:.2f}")
    else:
        print("A idade informada precisa ser válida!")

# Execução do programa
main()  
