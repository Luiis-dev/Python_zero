# Exercicio 20

# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

from random import shuffle # shuffle() # função que embaralha uma lista
alunos = str(input("Digite o nome dos quatro alunos: "))
ordem_de_apresenta = alunos.split() 
shuffle(ordem_de_apresenta)
print("A ordem de apresentação será:")
print(ordem_de_apresenta)

# Resposta do Guaanabara

import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será ")
print(lista)
