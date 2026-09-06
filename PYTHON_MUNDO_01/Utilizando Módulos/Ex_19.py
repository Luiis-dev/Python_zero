# Exercicio 19

# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice  # choice() # função que escolhe um elemento aleatório de uma lista
alunos = str(input("Digite o nome dos quatro alunos: "))
lista_alunos = alunos.split(",")  # split() # função que separa uma string em uma lista, usando um separador
pro_escolhe = choice(lista_alunos)
print("O Professor escolheu pra apagar o quadro {}.".format(pro_escolhe))

# Resposta de Guanabara

import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))
