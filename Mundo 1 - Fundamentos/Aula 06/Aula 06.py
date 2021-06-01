# Curso Python #06 - Tipos Primitivos e Saída de Dados

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {0} e {1} vale {2}.'.format(n1, n2, s))

n = input('Digite algo: ')
print(n.isnumeric())

# Metodos de Teste de Tipo de Strings

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculo?', a.isupper())
print('Está em minúsculo?', a.islower())
print('Está capitalizada?', a.istitle())

# title -> Nem maiúscula nem minúscula
 