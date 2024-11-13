# Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em true, escreva: "Você escapou!"

norte = False
sul = False
leste = False
oeste = True

if ( norte or sul or leste or oeste ):
    print('Você fugiu!')
else:
    print('Você está preso aqui!')