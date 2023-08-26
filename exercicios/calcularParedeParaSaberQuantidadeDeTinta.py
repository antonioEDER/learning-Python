# Desafio: Crie um algoritmo que leia a largura e altura de uma parede em metros.
# e calcule a área e a quantidade de tinta necessária.
# sabendo que 1 litro de tinta pinta uma área de 2mˆ2

largura = int(input('Declara o valor para largura: '))
altura = int(input('Declara o valor para altura: '))
 
area = altura*largura
litros = area / 2

print('A largura {} e altura {} é igual a uma área de {} \n  É necessário {:.2f} litros de tinta'.format(largura, altura, area, litros))
