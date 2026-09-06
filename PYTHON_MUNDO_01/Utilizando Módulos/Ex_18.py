#  Exercicio 18 

# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo


from math import radians
angulo = float(input("Digite um angulo:  "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O ângulo digitado foi {} e o sen {}, cos {} e tan {}".format(angulo, sen, cos, tan))

# Resposta do Guanabara

import math
ângulo = float(input("Digite um ângulo:  "))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))

# Outro jeito de fazer

from math import radians, sin, cos, tan
ângulo = float(input("Digite um ângulo:  "))
seno = sin(radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(ângulo, seno))
cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(ângulo, tangente))

