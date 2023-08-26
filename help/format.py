algo = ''

# :20 espaçamento
print('{:20}'.format(algo))

# :20 espaçamento e alinhamento a esquerda
print('{<:20}'.format(algo))

# :20 espaçamento e alinhamento aao centro
print('{:ˆ20}'.format(algo))

# :20 espaçamento e alinhamento aao centro
print('{=:ˆ20}'.format(algo)) # ===Ana===

# 3 casas decimais
print('{:.3f}'.format(algo))

# evitar a quebra de linha
print('{:.3f}'.format(algo, end=""))

# evitar a quebra de linha
print('{:.3f}'.format(algo, end=""))

# a quebra de linha
print('{:.3f} \n'.format(algo))

