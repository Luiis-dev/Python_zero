import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}.".format(num, math.ceil(raiz)))

# import math = importando toda a biblioteca
# ceil() arredonda para cima

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}.".format(num, math.floor(raiz)))

# floor() arredonda para baixo

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print("A raiz de {} é igual a {:.2f}.".format(num, floor(raiz)))

# from math import sqrt, floor = importando apenas as funções sqrt e floor
