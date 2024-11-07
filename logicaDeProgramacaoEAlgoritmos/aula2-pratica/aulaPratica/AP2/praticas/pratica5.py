# Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um ano bissexto"\

ano = int(input('Digite o ano para verificar se é bissexto: '))

if ( ano % 4 == 0 ):
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')