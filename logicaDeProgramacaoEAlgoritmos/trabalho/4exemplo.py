# EXIGÊNCIA DE CÓDIGO 1: Mensagem de boas-vindas com o nome completo
print("Bem-vindos à lista de contatos do [Seu Nome Completo]")

# EXIGÊNCIA DE CÓDIGO 2: Lista de contatos e variável global de ID
lista_contatos = []
id_global = 123456  # Substituir pelo seu RU

# EXIGÊNCIA DE CÓDIGO 3: Função para cadastrar contato
def cadastrar_contato(id):
    nome = input("Informe o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")
    contato = {"id": id, "nome": nome, "atividade": atividade, "telefone": telefone}
    lista_contatos.append(contato.copy())
    print("Contato cadastrado com sucesso!")

# EXIGÊNCIA DE CÓDIGO 4: Função para consultar contatos
def consultar_contatos():
    while True:
        opcao = input("\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Atividade\n4. Retornar ao menu\nEscolha uma opção: ")
        if opcao == "1":
            for contato in lista_contatos:
                print(contato)
        elif opcao == "2":
            id_consulta = int(input("Informe o ID do contato: "))
            encontrado = next((c for c in lista_contatos if c["id"] == id_consulta), None)
            print(encontrado if encontrado else "Contato não encontrado.")
        elif opcao == "3":
            atividade_consulta = input("Informe a atividade: ")
            contatos_filtrados = [c for c in lista_contatos if c["atividade"] == atividade_consulta]
            if contatos_filtrados:
                for c in contatos_filtrados:
                    print(c)
            else:
                print("Nenhum contato encontrado para essa atividade.")
        elif opcao == "4":
            return
        else:
            print("Opção inválida.")

# EXIGÊNCIA DE CÓDIGO 5: Função para remover contato
def remover_contato():
    while True:
        id_remover = int(input("Informe o ID do contato a ser removido: "))
        encontrado = next((c for c in lista_contatos if c["id"] == id_remover), None)
        if encontrado:
            lista_contatos.remove(encontrado)
            print("Contato removido com sucesso!")
            break
        else:
            print("Id inválido.")

# EXIGÊNCIA DE CÓDIGO 6: Menu principal
while True:
    opcao = input("\n1. Cadastrar Contato\n2. Consultar Contato\n3. Remover Contato\n4. Encerrar Programa\nEscolha uma opção: ")
    if opcao == "1":
        id_global += 1
        cadastrar_contato(id_global)
    elif opcao == "2":
        consultar_contatos()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

# EXIGÊNCIA DE SAÍDA DE CONSOLE
# Cadastro de contatos
cadastrar_contato(id_global)
id_global += 1
cadastrar_contato(id_global)
id_global += 1
cadastrar_contato(id_global)

# Consulta de todos os contatos
consultar_contatos()

# Consulta por ID
id_consulta = int(input("Informe o ID para consulta: "))
consultar_contatos()

# Consulta por atividade
atividade_consulta = input("Informe a atividade para consulta: ")
consultar_contatos()

# Remoção de um contato
remover_contato()
consultar_contatos()
