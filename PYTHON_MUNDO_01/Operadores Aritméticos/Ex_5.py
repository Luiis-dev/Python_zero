# Exercicio 5

# "Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor".

referente = int(input("Digite um número: "))
sucessor = referente + 1
antecessor = referente - 1 
print("O Valor do Referente é {}, sendo o seu Sucessor {} e seu Antecessor {}.".format(referente, sucessor, antecessor))

# Resposta do Guanabara
n = int(input("Digite um número: "))
a = n - 1
s = n + 1
print("Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}".format(n, a, s))

# outra forma de fazer também
n = int(input("Digite um número: "))
print("O antecessor de {} é {} e o sucessor é {}".format(n, (n-1), (n+1)))




