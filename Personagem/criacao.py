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

    personagem = {'Nome': nome,
                  'Classe': classe,
                  'vida': vida,
                  'ataque': ataque
                  }

    return personagem