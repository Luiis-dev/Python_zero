# Exercicio 11

# Faça um programa que leia a largura e a altura de uma 
# parede em metros, calcule a sua área e a quantidade de 
# tinta necessária para pintá-la, sabendo que cada litro 
# de tinta pinta uma área de 2 metros quadrados.

# largura = float(input("Digite a largura da parede: "))
# altura = float(input("Digite a altura dela: "))
# area = largura * altura
# tinta = area / 2
# print("A área da parede é {} metros quadrados.".format(area))
# print("Você precisará de {} litros de tinta.".format(tinta))

# Resposta do Guanabara
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
