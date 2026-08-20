class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self._vida = vida
        self.ataque = ataque

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        else:
            self._vida = valor

    def receber_dano(self, dano):
        self.vida -= dano

    def atacar(self, heroi):
        heroi.receber_dano(self.ataque)

        print(f'{self.nome} atacou {heroi.nome}')
        print (f'{self.nome} deu {self.ataque} de dano')
        print(f'O Herói {heroi.nome} está com HP {heroi.vida}')

def criar_inimigo():
    print('-'*20)
    print('UM SLIME APARECEU !!')
    print('-'*20)

    inimigo=Inimigo('Slime', 200, 35)
    return inimigo