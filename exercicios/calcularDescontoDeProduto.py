# Desafio: Crie um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

valor = float(input('Declara o valor do produto: '))

print('O produto de valor R$ {} tem um desconto de 5% \n O valor com desconto é igual a R$ {}'.format(valor, valor-(5/100) * valor))
