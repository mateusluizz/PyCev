# Desafio 03

"""
Crie um script Python que leia dois números e tente mostrar a soma entre eles.
"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))

# Ocorre a concatenação se os valores de n1 e n2 não forem declarados como inteiros(int)
# Como por exemplo

n1 = (input('Digite um valor: '))
n2 = (input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))
