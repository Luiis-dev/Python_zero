# Exercicio 8 

# "Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros."

# metros = float(input("Digite o valor do metro: "))
# centimetros = metros * 100
# milimetros = metros * 1000
# print("O Metro do valor digitado é {}m, O Centímetros é {}cm, e o Milímetros e {}mm".format(metros, centimetros, milimetros))

# Resposta do Guanabara

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

# {:.0f} -> significa que o número será formatado sem casas decimais.

# Desafio a mais 

medida = float(input("Digite o valor da medida: "))
km = medida * 1000
hm = medida * 100
dam = medida * 10
m = medida * 1  # ou nada
dm = medida / 10 # ou 0.1
cm = medida / 100 # ou 0.01
mm = medida / 1000 # ou 0.001
print("A medida digitada foi {}, sendo convertida em km foi {}km".format(medida, km))
print("A medida digitada foi {}, sendo convertida em hm foi {}hm".format(medida, hm))
print("A medida digitada foi {}, sendo convertida em dam foi {}dam".format(medida, dam))
print("A medida digitada foi {}, sendo convertida em m foi {}m".format(medida, m))
print("A medida digitada foi {}, sendo convertida em dm foi {}dm".format(medida, dm))
print("A medida digitada foi {}, sendo convertida em cm foi {}cm".format(medida, cm))
print("A medida digitada foi {}, sendo convertida em mm foi {}mm".format(medida, mm))
