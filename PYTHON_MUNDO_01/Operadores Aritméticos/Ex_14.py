# Exercicio 14

# "Escreva um programa que converta uma 
# temperatura digitada em °C e converta para °F."

temp = float(input("Digite a temperatura que deseja converter: ℃"))
conversor = (temp * 1.8) + 32
print("A temperatura de {}°C corresponde a {}°F".format(temp, conversor))
# Com ordem de precedência, a multiplicação é feita antes da soma, então não é necessário o uso de parênteses.

# Resposta do Guanabara

c = float(input('Informe a temperatura em °C: '))
f = ((c * 9)/5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
# Sem ordem de precedência, a multiplicação é feita antes da soma, então não é necessário o uso de parênteses.
