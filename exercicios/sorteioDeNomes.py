# Faça um programa para sortear 1 dos 4 alunos 
# Faça um programa para ranquear os ganhadores

import random

listaAlunos = ["Luna", "George", "Tom", "Rabubi"]

sorteio1 = random.choice(listaAlunos)
print('O aluno sorteado no primeiro sorteio é {} \n'.format(sorteio1))

sorteio2 = listaAlunos
random.shuffle(sorteio2)

print('Os alunos sorteados no segundo sorteio são: ')
for posicao, aluno in enumerate(sorteio2):
    print('{}-{}'.format(posicao+1, aluno))

