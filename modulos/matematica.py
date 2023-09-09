from math import ceil, floor, sqrt

num = int(input('Digite um número '))
raiz = sqrt(num)

print('A raiz do {} é igual a {} '.format(num, raiz))
print('A raiz do {} é igual a {:.2f} com abreviação '.format(num, raiz))
print('A raiz do {} é igual a {} arredontado para cima'.format(num, ceil(raiz)))
print('A raiz do {} é igual a {} arredontado para baixo'.format(num, floor(raiz)))