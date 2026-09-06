# 17 Exercício 

# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjecente de um triângulo retângulo, calcule
# mostre o comprimento da hipotenusa.

from math import hypot
comprimento_cateto = float(input("Digite o comprimento do cateto: "))
comprimento_cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = hypot (comprimento_cateto, comprimento_cateto_adjacente)
print("A hipotenusa vai medir {}".format(hipotenusa))

# Resposta do Guanabara

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))

# importando a função hypot() da biblioteca math

import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))


