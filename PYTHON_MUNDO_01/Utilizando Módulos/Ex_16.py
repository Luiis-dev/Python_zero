# Exercício 16 

# Crie um programa que leia um número real qualquer
# e mostre na tela a sua porção inteira.

from math import floor
n1 = float(input("Digite um número:  "))
numero = floor(n1)
print("O número digitado foi {} e a sua porcão inteira é {}".format(n1, numero))
