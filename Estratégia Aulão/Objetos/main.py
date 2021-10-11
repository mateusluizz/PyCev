from pessoa import Pessoa

p1 = Pessoa('Mateus', 27)
p2 = Pessoa('Maria', 30)
p3 = Pessoa('João', 32)

print(p1.nome)
print(p2.idade)

p1.falar('poo')
p2.falar('filmes')
p3.comer('Churrasco')
print(p1.ano_hoje)
print(p1.ano_atual)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p3.get_ano_nascimento())