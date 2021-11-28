# Desafio Python #009 - Tabuada

"""
DESAFIO 009
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

c = {'bf': '\033[1;97m',  # Branco forte
     'vermf': '\033[1;31m',  # Vermelho forte
     'am': '\033[33m',  # Amarelo
     'azft': '\033[1;34m',  # Azul forte
     'rf': '\033[1;35m',  # Roxo/rosa forte
     'l': '\033[m'}  # Limpar

n = int(input('{}Digite um número: '.format(c['am'])))
print('\n{} Tabuada do número {}\n'.format(c['azft'], n))
print('\033[1m' + '-' * 12)
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 0, c['rf'], c['vermf'], n * 0))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 1, c['rf'], c['vermf'], n * 1))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 2, c['rf'], c['vermf'], n * 2))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 3, c['rf'], c['vermf'], n * 3))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 4, c['rf'], c['vermf'], n * 4))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 5, c['rf'], c['vermf'], n * 5))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 6, c['rf'], c['vermf'], n * 6))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 7, c['rf'], c['vermf'], n * 7))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 8, c['rf'], c['vermf'], n * 8))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 9, c['rf'], c['vermf'], n * 9))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 10, c['rf'], c['vermf'], n * 10))
print('\033[1m' + '-' * 12)

a = int(input(f'{c["bf"]}Digite um número para ver sua tabuada: {c["l"]}'))
b = int(0)
print('\033[1m' + '-' * 12, '\033[m')
print(a, 'x', ' {:2} = {}'.format(b, b))
print(a, 'x', ' {:2} = {}'.format(b+1, a))
print(a, 'x', ' {:2} = {}'.format(b+2, a*2))
print(a, 'x', ' {:2} = {}'.format(b+3, a*3))
print(a, 'x', ' {:2} = {}'.format(b+4, a*4))
print(a, 'x', ' {:2} = {}'.format(b+5, a*5))
print(a, 'x', ' {:2} = {}'.format(b+6, a*6))
print(a, 'x', ' {:2} = {}'.format(b+7, a*7))
print(a, 'x', ' {:2} = {}'.format(b+8, a*8))
print(a, 'x', ' {:2} = {}'.format(b+9, a*9))
print(a, 'x', ' {:2} = {}'.format(b+10, a*10))
print('\033[1m' + '-' * 12, '\033[m')
