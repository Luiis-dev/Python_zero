# Exercico 21

# faça um programa em python que abra 
# e reproduza o áudio de um arquivo mp3

import os

pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_mp3 = os.path.join(pasta_script, "Escondido Em Mim.mp3")

os.startfile(caminho_mp3)