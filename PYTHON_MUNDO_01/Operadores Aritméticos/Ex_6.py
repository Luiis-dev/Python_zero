# Exercicio 6

# "Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada."

algoritmo = int(input("Digite um número: "))
dobro = algoritmo * 2
triplo = algoritmo * 3
raiz = algoritmo ** 0.5
print("O Dobro de {} é {}".format(algoritmo, dobro))
print("O Triplo de {} é {}".format(algoritmo, triplo))
print("A Raiz Quadrada de {} vai ser {:.2f}".format(algoritmo, raiz))

# Resposta do Guanabara

n = int(input('Digite um número: '))
d = n * 2 
t = n * 3 
r = n ** (1/2)
print("O dobro de {} vale {}.".format(n, d))
print("O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.".format(n, t, n, r))

# quebra de linha é essa que o Guanabara fez

print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(n, t, n, r))

# outra forma de fazer também direto
n = int(input("Digite um número: "))
print("O dobro de {} vale {}.".format(n, (n * 2)))
print("O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.".format(n, (n * 3), n, (n ** (1/2))))

# outra forma usando o pow
n = int(input("Digite um número: "))
print("O dobro de {} vale {}.".format(n, (n * 2)))
print("O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.".format(n, (n * 3), n, pow(n, (1/2))))

# pow calcula a raiz quadrada
# 1/2 é a fração (1 dividido por 2)
