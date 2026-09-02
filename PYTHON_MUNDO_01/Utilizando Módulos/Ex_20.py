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