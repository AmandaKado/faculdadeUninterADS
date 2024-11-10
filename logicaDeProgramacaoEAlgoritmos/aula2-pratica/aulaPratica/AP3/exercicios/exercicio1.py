"""
Realize a sequencia de print com for e while:
a) Inteiros de 3 até 12, com 12 incluso
b) Inteiros de 0 até 9, excluindo 9, com passo de 2 
"""

print('_' * 100)

for i in range (3, 13, 1 ):
    print(i)
    
x = 0

print('_' * 100)

while( x < 10 ):
    print(x)
    x += 1
    
print('_' * 100)

for i in range (0, 10, 1):
    print(i)    

print('_' * 100)

y = 3
while(y <= 12):
    print(y)
    y += 1

print('_' * 100)
