def existeArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt') as _:
            pass
    except FileNotFoundError:
        return False
    return True

def abrirArquivoLeitura(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'r')
    except Exception as e:
        print(f"Não foi possível abrir para leitura: {e}")
        return None
    else:
        print(f"Arquivo {nomeArquivo} aberto com sucesso!\n")
        return arquivo

def criarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'wt+') as _: pass
    except Exception as e:
        print(f"Erro na criação do arquivo: {e}")
    else:
        print(f"Arquivo {nomeArquivo} criado com sucesso! ")

def listarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt') as arquivo:
            dados = [linha.strip().split(';') for linha in arquivo.readlines()]
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []
    return dados

def inserir_dados(nomeArquivo, nomeJogador, score):
    try:
        with open(nomeArquivo, 'at') as arquivo:
            arquivo.write(f'{nomeJogador};{score}\n')
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")