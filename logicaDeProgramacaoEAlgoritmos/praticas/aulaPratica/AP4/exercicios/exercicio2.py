"""
Suponha que voce é um colecionador de jogos de videograme. Escreva um algoritmo que permita cadastrar esses jogos informando o nome e a qual videogame ele pertence

Para isso, crie um menu de opcoes contendo:

cadastrar novo item
listar tu do que foi cadastrado
sair

Para resolver esse exercicio, crie pelo menos uma funcao para cada item do menu

Alem disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados
"""\
    
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input( pergunta))
    return x

def existe_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def criar_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()
        
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else: 
        print(a.read())
    finally:
        a.close()

# Programa principal

arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criar_arquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar um novo item')
    print('2 - Listar os cadastros')
    print('3 - sair')
    
    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if(op == 1): # Novo item
        print('Opção de cadastrar novo item selecionada...')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif(op == 2): # Listar
        print('Opção de listar selecionada...')
        
        listarArquivo(arquivo)
    elif(op == 3): # Sair
        print('Encerrando...')
        break