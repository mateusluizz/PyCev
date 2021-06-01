# Exercício Python #007 - Média Aritmética

"""
DESAFIO 007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
media = (a+b)/2
if media >= 7:
    corm = '\033[1;32m'  # corm = cor da média 32 - verde, 31 - vermelho
else:
    corm = '\033[1;31m'
print(f'\nA \033[1;34mmédia\033[m entre \033[35m{a:.2f}\033[m e \033[35m{b:.2f}\033[m é {media:.2f}\033[m.')
print(f'\nA média entre {a:.2f} e {b:.2f} é igual a {media:.2f}')
