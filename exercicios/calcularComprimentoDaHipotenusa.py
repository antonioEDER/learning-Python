from math import hypot 

# Faça um programa que leia um [comprimento de cateto oposto] e do [cateto adjacente] de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

co = float(input('Comprimento do cateto oposto :'))
ca = float(input('Comprimento do cateto adjacente: '))

#calculo igual (co ** 2 + ca ** 2) ** (1/2)

hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))