#EMPRESSÕES ALGÉBRICAS

#somar 5 numeros
print( 1 + 2 + 3 + 4 + 5 )
#somar a media dos numeros 23, 19 e 31
print( (23 + 19 + 31) / 3 )
#o numero de vezes que o numero 73 cabe em 403
print( 403 // 73 )
#A sobra quando 403 é dividido por 73
print( 403 % 73 )
#2 elevado à 10 potencia
print( 2 ** 10 )
#o valor absoluto da diferença entre 54 e 57
print( abs(54 - 57) )
#menor valor entre 34,29 e 31
print( min(34, 29, 31) )

#ATRIBUIÇÃO

#atribuir o valor inteiro 3 á variavel a
a = 3
#atribuir o valor 4 à variável b
b = 4
#atribuir à variável c o valor da empressão a*b + b*b 
c = a * a + b * b

print(c)

#STRINGS

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# 'ant bat cod'
print(f'{s1} {s2} {s3}')
# 'ant ant ant ant ant ant ant ant ant ant'
print( (s1 + ' ') * 10 )
# 'ant bat bat cod cod cod'
print(f'{s1} ' + f'{s2} ' * 2 + f'{s3} ' * 3 )
# 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(f'{s1} {s2} ' * 7)
# 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print(f'{s2*2}{s3} ' * 5)


