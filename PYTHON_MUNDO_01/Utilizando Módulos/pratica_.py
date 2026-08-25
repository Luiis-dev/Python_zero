from gettext import install
import math

import pip
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}.".format(num, math.ceil(raiz)))

# import math = importando toda a biblioteca
# ceil() arredonda para cima

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}.".format(num, math.floor(raiz)))

# floor() arredonda para baixo

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print("A raiz de {} é igual a {:.2f}.".format(num, floor(raiz)))

# from math import sqrt, floor = importando apenas as funções sqrt e floor

import random
num = random.random()
print(num)

# random.random() = gera um número float aleatório entre 0 e 1

import random
num = random.randint(1, 10)
print(num)

# random.randint(1, 10) = gera um número inteiro aleatório entre 1 e 10

import emoji
print(emoji.emojize("Python é :thumbs_up:")) # e

# emoji.emojize("Python é :thumbs_up:") = gera um emoji de acordo com o código passado
# thumbs_up = 👍
