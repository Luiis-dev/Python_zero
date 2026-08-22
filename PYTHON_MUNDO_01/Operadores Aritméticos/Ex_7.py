# Exercicio 7

# "Desenvolva um programa que leia as duas notas
# de um aluno, calcule e mostre a sua média."

nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua outra nota: "))
soma_das_notas = (nota_1 + nota_2 ) / 2
print("A Soma das suas Notas é {}".format(soma_das_notas))

# Resposta do Guanabara

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segundo nota do aluno: '))
media = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {}'.format(n1, n2, media))

# :.1f -> significa que o número será formatado com uma casa decimal.

