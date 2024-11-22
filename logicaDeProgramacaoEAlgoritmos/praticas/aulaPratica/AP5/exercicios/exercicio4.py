from datetime import datetime

# Dicionário para armazenar os cadastros
cadastro = {
    'nome': [],
    'sexo': [],
    'ano': []
}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N] ').strip().upper()
    if terminar == 'N':
        break
    if terminar != 'S':
        print('Digite S para SIM e N para NÃO!')
        continue

    nome = input('Nome: ').strip()
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('Digite M para Masculino ou F para Feminino!')
        sexo = input('Sexo [M/F]: ').strip().upper()

    try:
        ano = int(input('Ano de nascimento: ').strip())
        if ano < 1900 or ano > datetime.now().year:
            raise ValueError
    except ValueError:
        print('Ano inválido. Tente novamente.')
        continue

    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)

# Análise dos dados cadastrados
total_cadastros = len(cadastro['nome'])
idades = [datetime.now().year - ano for ano in cadastro['ano']]
media_idades = sum(idades) / total_cadastros if total_cadastros > 0 else 0

# Lista de mulheres com menos de 30 anos
mulheres_menores_30 = [
    cadastro['nome'][i] for i in range(total_cadastros)
    if cadastro['sexo'][i] == 'F' and idades[i] < 30
]

# Lista de homens com idade acima da média
homens_acima_media = [
    cadastro['nome'][i] for i in range(total_cadastros)
    if cadastro['sexo'][i] == 'M' and idades[i] > media_idades
]

# Exibição dos resultados
print("\n=== Resultados ===")
print(f"Total de cadastros: {total_cadastros}")
print(f"Média das idades: {media_idades:.2f}")
print(f"Mulheres com menos de 30 anos: {', '.join(mulheres_menores_30) if mulheres_menores_30 else 'Nenhuma'}")
print(f"Homens com idade acima da média: {', '.join(homens_acima_media) if homens_acima_media else 'Nenhum'}")
