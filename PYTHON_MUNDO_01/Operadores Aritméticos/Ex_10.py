# Exercicio 10

# "Crie um programa que leia quanto dinheiro uma pessoa 
# tem na carteira e mostre quantos dólares ela pode comprar."

# carteira = float(input("Digite o valor que vc tem na carteira: "))
# dolar = carteira / 5.22
# print("Eu tenho na minha carteira R${}, se fosse em dólar seria {:.2f}".format(carteira, dolar))

# Resposta do Guanabara

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))


