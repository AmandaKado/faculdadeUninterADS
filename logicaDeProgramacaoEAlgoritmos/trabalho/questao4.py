def exibir_desenvolvedor():
    print("\nBem vindos a lista de contatos da Amanda Mayumi Kado!\n")

# Função para exibir menu
def exibir_menu(): 
    while True:
        print("1) Cadastrar Contato")
        print("2) Consultar Contato")
        print("3) Remover Contato")
        print("4) Encerrar Programa\n")
        
        resposta = int(input("Envie somente o número [1, 2, 3, 4] >> "))
        
        try:
            match resposta:
                case 1:
                    print("1")
                    break
                case 2: 
                    print("2")
                    break
                case 3: 
                    print("3")
                    break
                case 4:
                    print("4")
                    break
                case _:
                    print("\nValor inválido! Insira um número válido\n")
                    continue
        except ValueError:
            print("Insira um número de 1 à 4!\n")
            continue
        break

# Código principal para execuução do programa
exibir_desenvolvedor()

exibir_menu()
