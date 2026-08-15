from random import randint

def atacar(heroi, vilao):
    vilao['vida'] -= heroi['ataque']

    print(f'{heroi["Nome"]} atacou o {vilao["Nome"]}')
    print(f'{heroi["Nome"]} deu {heroi["ataque"]} de dano')

    if vilao['vida'] <= 0:
        vilao['vida'] = 0
    else:
        print(f'Agora o {vilao["Nome"]} está com HP: {vilao["vida"]}')


def ataque_inimigo(vilao, heroi):
    heroi['vida'] -= vilao['ataque']

    print(f'{vilao["Nome"]} atacou o {heroi["Nome"]}')
    print (f'{vilao["Nome"]} deu {vilao["ataque"]} de dano')

    if heroi['vida'] <= 0:
        heroi['vida'] = 0
    else:
        print(f'O Herói {heroi["Nome"]} está com HP: {heroi["vida"]}')



def batalha(heroi, inimigo):
    while heroi['vida'] > 0 and inimigo['vida'] > 0:
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
            atacar(heroi, inimigo)
            if  inimigo['vida']  <= 0:
                print('Parabéns, você venceu !')
                break
            ataque_inimigo(inimigo, heroi)
            if heroi['vida'] <= 0:
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
                ataque_inimigo(inimigo, heroi)
                if heroi['vida'] <= 0:
                    print('Você perdeu mo')
                    break

        else:
            print('Opcao invalida, digite 1, 2 ou 3:')

def mostrar_status(heroi,vilao):
    print('-'*20,'STATUS'.center(20),'-'*20)
    print('Nome:', heroi["Nome"])
    print('Classe:', heroi["Classe"])
    print('HP:', heroi["vida"])
    print('Ataque:', heroi["ataque"])
    print('-'*20)
    print()

    print('Monstro:', vilao["Nome"])
    print('HP:', vilao["vida"])
    print('Ataque:', vilao["ataque"])

    print('-' * 20)