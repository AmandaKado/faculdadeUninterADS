# Função para exibir o nome do desenvolvedor
def exibir_desenvolvedor():
    print("\nBem-vindos à lista de contatos da Amanda Mayumi Kado!\n")

lista_contatos = [""]
id_global = 5069371

# Função para cadastrar contato
def cadastrar_contato(id):
    nome = input("Nome: ")
    atividade = input("Atividade: ")
    telefone = int(input("Telefone: "))

    # Armazena os dados inseridos dentro de um dicionário
    contato = {id, nome, atividade, telefone}
    
    # Copia os dados do dicionario para a variável lista_contatos
    lista_contatos.copy(contato)

# Função para exibir menu
def exibir_menu(): 
    while True:
        print("1) Cadastrar Contato")
        print("2) Consultar Contato")
        print("3) Remover Contato")
        print("4) Encerrar Programa\n")
        
        try:
            # Tenta converter a entrada para número inteiro
            resposta = int(input("Envie somente o número [1, 2, 3, 4] >> "))
            
            # Avalia a opção usando match-case
            match resposta:
                case 1:
                    print("Você escolheu: Cadastrar Contato")
                    cadastrar_contato(55868)
                    break
                case 2: 
                    print("Você escolheu: Consultar Contato")
                    break
                case 3: 
                    print("Você escolheu: Remover Contato")
                    break
                case 4:
                    print("Encerrando programa...")
                    break  # Sai do loop e encerra o programa
                case _:  # Caso para valores fora do intervalo esperado
                    print("\nValor inválido! Insira um número válido\n")
        except ValueError:  # Trata erro ao converter entrada para inteiro
            print("Erro: Insira um número válido de 1 a 4!\n")
            continue  # Reinicia o loop para pedir uma nova entrada

# Código principal para execução do programa
exibir_desenvolvedor()
exibir_menu()
