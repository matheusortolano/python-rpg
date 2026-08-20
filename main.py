from Personagem.criacao import criar_personagem
from Vilao.Slime import criar_inimigo
from batalha import *
heroi = criar_personagem()
vilao = criar_inimigo()

batalha(heroi, vilao)