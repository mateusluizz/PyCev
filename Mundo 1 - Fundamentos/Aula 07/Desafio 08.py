# Desafio Python #008 - Conversor de Medidas

"""
DESAFIO 008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e mílimetros.
Unidades de medida: km, hm, dam, m, dm, cm, mm.
"""

a = float(input('Digite um valor em metros: '))
print(f'{a:.2f}m equivalem a: \n{a/100}km, \n{a/100}hm, \n{a/10}dam,')
print(f'{a*10}dm, \n{a*100}cm e \n{a*1000}mm')
