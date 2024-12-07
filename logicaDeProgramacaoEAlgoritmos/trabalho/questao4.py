# Exibe uma mensagem de boas-vindas com o nome do desenvolvedor
print("\n Bem vindos à lista de contatos de Amanda Mayumi Kado\n")

# Lista para armazenar os dados dos contatos
lista_contatos = []
id_global = 5069371  # ID inicial baseado no meu RU

# Função para estilizar menus

def estilo_menu():
    print("\n","*" * 52)

# Função para cadastrar um novo contato
def cadastrar_contato(id):
    """
    Cadastra um contato com nome, atividade e telefone.
    O ID é fornecido como argumento e é único para cada contato.
    """    
    print(" ****************** MENU CADASTRO ******************* \n")
    
    print(f"Id do Contato: {id}")
    nome = input(" Por favor entre com o nome do Contato: ")
    atividade = input(" Por favor entre com a Atividade do contato: ")
    telefone = input(" Por favor entre com o Telefone do contato: ")
    
    # Criação do dicionário do contato
    contato = {
        "id": id,  # Atribui o ID único ao contato
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    # Adiciona o dicionário do contato à lista de contatos
    lista_contatos.append(contato.copy())

# Função para consultar contatos
def consultar_contatos():
    """
    Permite consultar contatos cadastrados de diferentes formas e
    retorna ao menu principal ao escolher a opção correspondente.
    """
    print(" **************** MENU DE CONSULTA ****************** \n")
    
    while True:
        # Menu de opções de consulta
        try:
            resposta = int(input(" Selecione a opção desejada: \n\n 1 - Consultar Todos\n 2 - Consultar por ID\n 3 - Consultar por Atividade\n 4 - Retornar ao menu \n\n >> "))
        except ValueError:
            print(" Opção inválida! Por favor, insira um número de 1 à 4.")
            continue
        
        match resposta:
            case 1:
                # Mostra todos os contatos cadastrados
                if lista_contatos:
                    print(" Contatos cadastrados:")
                    for contato in lista_contatos:
                        print(f"\n Id: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
                else:
                    print(" Nenhum contato cadastrado.")
                continue
            
            case 2:
                # Consulta por ID
                try:
                    id = int(input(" Informe o ID do contato: "))
                    encontrado = False
                    for contato in lista_contatos:
                        if contato["id"] == id:
                            print(" Contato encontrado:", contato)
                            encontrado = True
                            break
                    if not encontrado:
                        print(" Contato com ID informado não encontrado. Verifique se inseriu o ID correto.")
                except ValueError:
                    print(" Por favor, insira um ID válido.")
                continue
            
            case 3:
                # Consulta por atividade
                atividade = input(" Informe a atividade: ")
                # Filtra contatos pela atividade fornecida
                encontrados = [contato for contato in lista_contatos if contato["atividade"].lower() == atividade.lower()]
                
                if encontrados:
                    print(" Contatos encontrados para a atividade", atividade + ":")
                    for contato in encontrados:
                        print(f"\n Id: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}")
                else:
                    print(" Nenhum contato encontrado para a atividade informada.")
                continue
            
            case 4:
                # Retorna ao menu principal
                print(" Retornando ao menu principal...")
                return
            
            case _:
                print(" Opção inválida! Tente novamente.")

# Função para remover um contato pelo ID
def remover_contato():
    """
    Remove um contato da lista com base no ID fornecido.
    Solicita o ID repetidamente até que um ID válido seja informado.
    """
    print(" ************ MENU DE REMOÇÃO DE CONTATO ************ \n")
    
    while True: 
        try:
            # Solicita o ID do contato a ser removido
            id_remove = int(input(" Informe o ID do contato a ser removido: "))
            
            # Verifica se o ID existe na lista de contatos
            for contato in lista_contatos:
                if contato["id"] == id_remove:
                    lista_contatos.remove(contato)
                    print(f" Contato com ID {id_remove} foi removido com sucesso!")
                    return  # Sai da função após remover o contato
            
            # Caso o ID não seja encontrado
            print(" ID inválido.")
        
        except ValueError:
            print(" Por favor, insira um ID válido.")

# Código principal do programa
while True:
    try:
        estilo_menu()
        
        # Exibe o menu principal
        resposta = int(input(" ****************** MENU PRINCIPAL******************* \n\n Escolha a opção desejada:\n\n 1 - Cadastrar Contato\n 2 - Consultar Contato(s)\n 3 - Remover Contato\n 4 - Sair\n\n >> "))
        
        estilo_menu()
        
        match resposta:
            case 1:
                # Incrementa o ID global e cadastra um novo contato
                id_global += 1
                cadastrar_contato(id_global)
            case 2:
                # Chama a função de consulta de contatos
                consultar_contatos()
            case 3:
                # Chama a função para remover um contato
                remover_contato()
            case 4:
                # Encerra o programa
                print(" Encerrando programa...")
                break
            case _:
                # Trata entradas inválidas
                print(" Opção inválida! Selecione um número de 1 à 4")
                continue
    except ValueError:
        print(" Opção inválida! Selecione um número de 1 à 4")
