# Desafio: Crie um algoritmo que leia um número inteiro e mostre a sua tabuada

numero = int(input('Declare um número: '))
tabuada = ""

for num in range(1, 11):
    tabuada += '{} x {} = {} \n'.format(num, numero, numero*num)


print('Para o número {}  a tabuada é.. \n {}'.format(numero, tabuada))
