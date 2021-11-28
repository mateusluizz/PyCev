# Desafio Python #005 - Antecessor e Sucessor

"""
DESAFIO 005
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

a = float(input('Digite um número: '))
b = a - 1
c = a + 1
print(f'Analisando o valor {a:.0f}, seu antecessor é {a-1:.0f} e o sucessor é {a+1:.0f}.')
print(f'Analisando o valor {a:.0f}, seu antecessor é {b:.0f} e o sucessor é {c:.0f}.')
