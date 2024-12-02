def exibir_desenvolvedor():
    print("\nBem-vindos a Madeireira da Lenhadora Amanda Mayumi Kado\n")

def escolha_tipo():
    tipos = {
        "PIN": 150.40,
        "PER": 170.20,
        "MOG": 190.90,
        "IPE": 210.10,
        "IMB": 220.70
    }
    
# Função de escolha do tipo de madeira desejado
    while True:
        print("\nTipos de madeira disponíveis:")
        print("\n→ Tora de Pinho (PIN)")
        print("→ Tora de Peroba (PER)")
        print("→ Tora de Mogno (MOG)")
        print("→ Tora de Ipê (IPE)")
        print("→ Tora de Imbuia (IMB)\n")
        escolha = input("Envie somente a sigla do tipo de madeira: ").strip().upper()

        if escolha in tipos:
            return tipos[escolha]  # Retorna o valor correspondente ao tipo escolhido
        else:
            print("\nInsira um tipo de madeira válido!")

def qtd_toras():
    while True:
        metroQuadrado = float(input("Quantidade de toras: "))
        try:
            if metroQuadrado < 100:
                return metroQuadrado
                desconto = 0 / 100
                break
            elif metroQuadrado >= 100 and metroQuadrado < 500:
                return metroQuadrado
                desconto = 4 / 100
                break
            elif metroQuadrado >= 500 and metroQuadrado < 1000:
                return metroQuadrado
                desconto = 9 / 100
                break
            elif metroQuadrado >= 1000 and metroQuadrado < 2000:
                return metroQuadrado
                desconto = 16 / 100
                break
            elif metroQuadrado < 2000:
                print("Não é aceito pedidos acima de 2000 m³! \n")
            else:
                print("Valor inválido! Selecione uma quantidade de toras válida. \n")
                continue
        except ValueError:
            print("Valor inserido não válido! \n")

def transporte():
    deseja_transporte = input("Deseja serviço de transporte? [S/N] ").STR().upper()
    if deseja_transporte == "S":
        try:
            print("Opções de transporte: \ntransporte rodoviário (1)\ntransporte ferroviário (2)\ntransporte hidroviário (3)\n")
            
            selecao_transporte = int(input("Digite apenas o número para escolher o método de transporte: [1, 2, 3] "))
            
            if selecao_transporte == 1:
                valor_transporte = 1000
                return selecao_transporte 
            elif selecao_transporte == 2:
                valor_transporte = 2000
                return selecao_transporte 
            elif selecao_transporte == 3:
                valor_transporte = 3500
                return selecao_transporte 
            else:
                print("Valor inválido! \n")
        except:
            print("Insira um valor numérico! ")
    else:
        return None

def principal():
    exibir_desenvolvedor()
    escolha_tipo()
    qtd_toras()
    
principal()