# Exibe o desenvolvedor do sistema
print("Sistema desenvolvido por Amanda Mayumi Kado")

# Entrada do valor base do plano e da idade do cliente
valorBase = float(input("Insira o valor base do plano: "))
idade = int(input("Idade do cliente: "))

# Inicializa a variável de porcentagem
porcentagem = 0

# Calcula o valor mensal com base na faixa etária do cliente
if idade >= 0 and idade < 19:  # Faixa etária de 0 a 18 anos
    porcentagem = 100 / 100
elif idade >= 19 and idade < 29:  # Faixa etária de 19 a 28 anos
    porcentagem = 150 / 100
elif idade >= 29 and idade < 39:  # Faixa etária de 29 a 38 anos
    porcentagem = 225 / 100
elif idade >= 39 and idade < 49:  # Faixa etária de 39 a 48 anos
    porcentagem = 240 / 100
elif idade >= 49 and idade < 59:  # Faixa etária de 49 a 58 anos
    porcentagem = 350 / 100
elif idade >= 59:  # Faixa etária acima de 59 anos
    porcentagem = 600 / 100
else:
    # Idade inválida, exibe mensagem de erro e finaliza
    print("A idade informada precisa ser válida!")
    exit()

# Calcula o valor mensal do plano de saúde
valorMensal = valorBase * porcentagem

# Exibe o valor mensal do plano
print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
