def exibir_desenvolvedor():
    print("\nBem vindos a lista de contatos da Amanda Mayumi Kado!\n")

# Função para exibir menu
def exibir_menu(): 
    print("1) Cadastrar Contato")
    print("2) Consultar Contato")
    print("3) Remover Contato")
    print("4) Encerrar Programa\n")
    
    resposta = int(input(">> "))
    
    try:
        if resposta == 1:
            print("\nFoi escolhido o numero 1\n")
        elif resposta == 2:
            print("\nFoi escolhido o numero 2\n")
        elif resposta == 3:
            print("\nFoi escolhido o numero 3\n")
        elif resposta == 4:
            print("\nFoi escolhido o numero 4\n")
        else:
            print("\nValor inserido inválido! Envie um número de 1 à 4 de acordo com a opção desejada.\n")
    except ValueError:
        print("Insira um número de 1 à 4!\n")
    
# Código principal para execuução do programa
exibir_desenvolvedor()

exibir_menu()
