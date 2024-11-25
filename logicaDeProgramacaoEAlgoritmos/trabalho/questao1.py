# Print simples para mostrar quem desenvolveu o sistema:
print("Sistema desenvolvido por Amanda Mayumi Kado") 

# Variável 'valorBase', onde o valor é inserido pelo usuário:
valorBase = float(input("Insira o valor base do plano: ")) 
# Variável 'idade', onde o valor é inserido pelo usuário:
idade = int(input("Idade do cliente: ")) 
# Variável 'porcentagem' para armazenar a porcentagem de cobrança:
porcentagem = 0

# Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100):
if(idade >= 0 and idade < 19): # Verifica se idade está na faixa de 1 ~ 18
    porcentagem = 100 / 100
    valorMensal = valorBase * porcentagem
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
# Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100):
elif(idade >= 19 and idade < 29): # Verifica se idade está na faixa de 19 ~ 28 
    porcentagem = 150 / 100
    valorMensal = valorBase * porcentagem
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
# Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100):
elif(idade >= 29 and idade < 39): # Verifica se idade está na faixa de 29 ~ 38 
    porcentagem = 225 / 100
    valorMensal = valorBase * porcentagem
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
# Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100):
elif(idade >= 39 and idade < 49): # Verifica se idade está na faixa de 39 ~ 48 
    porcentagem = 240 / 100
    valorMensal = valorBase * porcentagem
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
# Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100):
elif(idade >= 49 and idade < 59): # Verifica se idade está na faixa de 49 ~ 58 
    porcentagem = 350 / 100
    valorMensal = valorBase * porcentagem
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
# Se a idade for maior ou igual que 59, o valor será de 600% do valor base do plano (600 / 100):
elif(idade >= 59): # Verifica se idade é superior a 59 
    porcentagem = 600 / 100
    valorMensal = valorBase * porcentagem
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
# Se valor de idade inserido não é válido, executa:
else:
    print("A idade informada precisa ser válida!")
