# Curso Python #07 - Operadores Aritméticos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2 # Soma
m = n1 * n2 # Multiplacação
d = n1 / n2 # Divisão
di = n1 // n2 # Divisão Inteira
e = n1 ** n2 # Exponenciação
print('A soma vale {}'.format(n1+n2))
print('A soma é {},\no produto é {},\na divisão é {:.2f}'.format(s, m, d), end=' >>> ')
print('A divisão inteira é {} e potência é {:.2f}'.format(di, e))

# Tipos de formatação

n = input('Qual seu nome? ')
print('Prazer em te conhecer {}!'.format(n))
print('Prazer em te conhecer {:20}!'.format(n)) # escrever em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(n)) # escrever em 20 espaços alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(n)) # escrever em 20 espaços alinhado a esquerda
print('Prazer em te conhecer {:^20}!'.format(n)) # escrever em 20 espaços centralizado
print('Prazer em te conhecer {:=^20}!'.format(n)) # escrever em 20 centralizado com '=' aos lados
print(f'Prazer em te conhecer {n:=^20}!') # escrever em 20 centralizado com '=' aos lados
print('Prazer em te conhecer {:&^20}!'.format(n)) # escrever em 20 centralizado com '&' aos lados
