# 17 Exercício 

# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjecente de um triângulo retângulo, calcule
# mostre o comprimento da hipotenusa.

from math import hypot
comprimento_cateto = float(input("Digite o comprimento do cateto: "))
comprimento_cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = hypot (comprimento_cateto, comprimento_cateto_adjacente)
print("A hipotenusa vai medir {}".format(hipotenusa))

