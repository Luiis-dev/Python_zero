import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}.".format(num, math.ceil(raiz)))

# ceil() arredonda para cima

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}.".format(num, math.floor(raiz)))

# floor() arredonda para baixo