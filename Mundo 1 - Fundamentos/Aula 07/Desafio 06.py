# Exercício Python #006 - Dobro, Triplo, Raiz Quadrada

"""
DESAFIO 006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

cores = {'bf': '\033[1;97m',  # Branco forte
         'vermf': '\033[1;31m',  # Vermelho forte
         'am': '\033[33m',  # Amarelo
         'azft': '\033[1;34m',  # Azul forte
         'rf': '\033[1;35m',  # Roxo/rosa forte
         'l': '\033[m'}  # Limpar

a = float(input('Digite um número: '))
dobro = a * 2
triplo = a * 3
sqrt = a ** (1/2)
print(f'O dobro de {a:.0f} vale {dobro:.0f} \nO triplo vale {triplo:.0f} \nA raiz quadrada vale {sqrt:.2f}')

print(f'\nO dobro de {cores["ru"]}{a}{cores["l"]} é {cores["amf"]}{a*2}{cores["l"]}.')
print(f'O triplo de {cores["ru"]}{a}{cores["l"]} é {cores["amf"]}{a*3}{cores["l"]}.')
print(f'A raiz quadrade de {cores["ru"]}{a}{cores["l"]} é {cores["amf"]}{pow(a, (1/2))}{cores["l"]}.')