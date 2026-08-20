from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, classe, vida, ataque):
        self.nome = nome
        self.classe = classe
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

    @abstractmethod
    def atacar(self,vilao):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome,'Guerreiro', 180, 55)

    def atacar(self, vilao):
        vilao.receber_dano(self.ataque)
        print(f"o {self.nome} atacou com Giro de Machado")

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome,'Mago', 100, 90)
    def atacar(self, vilao):
        vilao.receber_dano(self.ataque)
        print(f"o {self.nome} atacou com Bola de fogo")

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome,'Arqueiro', 130, 65)
    def atacar(self, vilao):
        vilao.receber_dano(self.ataque)
        print(f"o {self.nome} atacou com Chuva de flechas")

def criar_personagem():
    print('-'*15, 'Criação de Personagem', '-'*15)

    nome = input('Olá, aventureiro, como você se chama? ^^ : ').strip()

    print ('Classes disponiveis'
        '\n1 - Guerreiro'
        '\n2 - Mago'
        '\n3 - Arqueiro ')
    print()

    while True:
        try:
            classe = int(input('Qual classe gostaria de seguir? '))
        except ValueError:
            print('Digite apenas números.')
        else:
            if classe in (1, 2, 3):
                break
            else:
                print('Escolha apenas 1, 2 ou 3.')
    if classe == 1:
        classe = 'Guerreiro'
    elif classe == 2:
        classe =  'Mago'
    elif classe == 3:
        classe =  'Arqueiro'
    resp=str(input(f'Você confirma a classe {classe} [S/N]?'))
    if resp in 'Nn':
        print('Reinicie o programa e selecione sua classe...')
        exit()
    else:
        print('SEJA BEM VINDO!')
    print('-'*30)

    vida = ataque = 0

    if classe == 'Guerreiro':
        personagem = Guerreiro(nome)
    elif classe == 'Mago':
        personagem = Mago(nome)
    elif classe == 'Arqueiro':
        personagem = Arqueiro(nome)

    return personagem