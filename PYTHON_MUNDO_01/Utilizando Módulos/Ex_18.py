#  Exercicio 18 

# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo


from math import radians
angulo = float(input("Digite um angulo:  "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O ângulo digitado foi {} e o sen {}, cos {} e tan {}".format(angulo, sen, cos, tan))