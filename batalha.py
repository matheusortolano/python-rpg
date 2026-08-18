from random import randint

def batalha(heroi, inimigo):
    while heroi.vida > 0 and inimigo.vida > 0:
        try:
            acao = int(input('o que deseja fazer?'
                         '\n1 - Atacar'
                         '\n2 - Ver Status'
                         '\n3 - Fugir'
                         '\n'))
        except ValueError:
            print('Digite apenas numeros: ')
            continue

        if acao == 1:
            heroi.atacar(inimigo)
            if  inimigo.vida  <= 0:
                print('Parabéns, você venceu !')
                break
            inimigo.atacar(heroi)
            if heroi.vida <= 0:
                print('Parabéns, você perdeu !')
                break
        elif acao == 2:
            mostrar_status(heroi,inimigo)

        elif acao == 3:
            chance_fuga= randint(1,100)
            if chance_fuga <= 70:
                print('Fugindo...')
                break
            else:
                print('Fugir falhou mo :(')
                inimigo.atacar(heroi)
                if heroi.vida <= 0:
                    print('Você perdeu mo')
                    break

        else:
            print('Opcao invalida, digite 1, 2 ou 3:')

def mostrar_status(heroi,vilao):
    print('-'*20,'STATUS'.center(20),'-'*20)
    print('Nome:', heroi.nome)
    print('Classe:', heroi.classe)
    print('HP:', heroi.vida)
    print('Ataque:', heroi.ataque)
    print('-'*20)
    print()

    print('Monstro:', vilao.nome)
    print('HP:', vilao.vida)
    print('Ataque:', vilao.ataque)

    print('-' * 20)