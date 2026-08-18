class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, heroi):
        heroi.vida -= self.ataque

        print(f'{self.nome} atacou {heroi.nome}')
        print (f'{self.nome} deu {self.ataque} de dano')
        if  heroi.vida <= 0:
            heroi.vida = 0
        else:
            print(f'O Herói {heroi.nome} está com HP {heroi.vida}')

def criar_inimigo():
    print('-'*20)
    print('UM SLIME APARECEU !!')
    print('-'*20)

    inimigo=Inimigo('Slime', 200, 35)
    return inimigo