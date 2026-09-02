# Exercicio 19

# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice  # choice() # função que escolhe um elemento aleatório de uma lista
alunos = str(input("Digite o nome dos quatro alunos: "))
lista_alunos = alunos.split(",")  # split() # função que separa uma string em uma lista, usando um separador
pro_escolhe = choice(lista_alunos)
print("O Professor escolheu pra apagar o quadro {}.".format(pro_escolhe))
