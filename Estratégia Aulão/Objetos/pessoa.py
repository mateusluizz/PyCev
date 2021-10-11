from _datetime import datetime
from datetime import date

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    ano_hoje = date.today().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def get_nome(self):
        print(self.nome)

    def get_ano_nascimento(self):
        return self.ano_hoje - self.idade

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} parou de falar.')
            self.falando = False
            return

        print(f'{self.nome} não está falando.')
