# Exercício Python #010 - Conversor de Moedas

"""
DESAFIO 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. 31/05/2021

Considere US$1,00 = R$5,22

"""

a = float(input('Quanto dinheiro você tem na carteira? R$'))
real = a * 5.22
dolar = a / 5.22
print(f'\nCom {a:.2f} reais você pode comprar US${dolar:.2f} dólares')
print(f'Com {a:.2f} dólares você pode comprar R${real:.2f} reais\n')

print('\033[1;36mConversor de reais para moedas estrangeiras e criptomoeda bitcoin.')
r = float(input('\033[32mQuanto de dinheiro em reais você tem na carteira? R$'))  # Real
dol = r / 5.22  # Dólar (US$)
eur = r / 6.38  # Euro(€)
lb_est = r / 7.43  # Libra esterlina(£), moeda oficial do Reino Unido.
ien = r * 47.41  # Iene (¥)
btc = r / 194439.25  # Bitcoin (₿)
print(f'\033[1;30m\nConforme cotação de 31 de maio de 2021 com \033[1;32mR${r:.2f}\033[1;30m você pode comprar:')
print(f'\033[1;35;m\nUS${dol:.2f}\n€{eur:.2f}\n£{lb_est:.2f}\n¥{ien:.2f}\n₿{btc:.6f}\033[m')
print()
