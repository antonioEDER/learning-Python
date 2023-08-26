# Desafio: Crie um algoritmo que leia um valor em real e converta em dolar
# considerar USS 1.00 = R$ 3.27

real = float(input('Declara o valor em R$: '))

print('Você tem na carteira {} que é igual a {:.2f} dolar'.format(real, real/3.27))
