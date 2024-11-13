# Se dano é maior que 10 e escudo é igual a 0, escreva: "Você morreu!"
dano = float(input('Dano: '))
escudo = float(input('Escudo: '))

if ( dano > 10 and escudo <= 0 ):
    print('Você morreu!')
else:
    print('Você sobreviveu')
