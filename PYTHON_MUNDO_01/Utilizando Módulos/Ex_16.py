# Exercício 16 

# Crie um programa que leia um número real qualquer
# e mostre na tela a sua porção inteira.

from math import floor
n1 = float(input("Digite um número:  "))
numero = floor(n1)
print("O número digitado foi {} e a sua porcão inteira é {}".format(n1, numero))

# Resposta do Guanabara

import math
num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))

# Ou

from math import trunc
num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))

# Outra forma de fazer sem utilizar a matemática

num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é {}".format(num, int(num)))

