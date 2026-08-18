class Personagem:
    def __init__(self, nome, classe, vida, ataque):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque


    def atacar(self, vilao):
        vilao.vida -= self.ataque

        print(f'{self.nome} atacou o {vilao.nome}')
        print(f'{self.nome} deu {self.ataque} de dano')

        if vilao.vida <= 0:
            vilao.vida = 0
        else:
            print(f'Agora o {vilao.nome} está com HP: {vilao.vida}')


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
        vida = 180
        ataque = 55
    elif classe == 'Mago':
        vida = 100
        ataque = 90
    elif classe == 'Arqueiro':
        vida = 130
        ataque = 65

    personagem = Personagem(nome, classe, vida, ataque)
    return personagem