from Personagem.criacao import criar_personagem
from Vilao.Slime import criar_inimigo
from batalha import *
heroi = criar_personagem()
print(heroi)
vilao = criar_inimigo()
print(vilao)

batalha(heroi, vilao)