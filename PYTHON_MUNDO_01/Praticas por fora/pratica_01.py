# nivel 1 — Operadores básicos

# Questão 1

# Peça dois números ao usuário e mostre
# o resultado das 4 operações básicas (+, -, *, /). 

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
adicao = n1 + n2
subtracacao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
print(f"""
Adiçao: {adicao}
Subtração: {subtracacao}
Multiplicação: {multiplicacao}
Divisão: {divisao}
""") 

# Ou 

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
adicao = n1 + n2
subtracacao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
print(f"""Adiçao: {adicao}\nSubtração: {subtracacao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}""") 

# Ou

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
adicao = n1 + n2
subtracacao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
print("Adiçao: {}\nSubtração: {}\nMultiplicação: {}\nDivisão: {}".format(adicao, subtracacao, multiplicacao, divisao))


# Questão 2
 
# Calcule o resto e o quociente da 
# divisão entre dois números (use % e //).

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
resto_da_divisao = n1 % n2
divisao_inteira = n1 // n2
print("O Resto da divisão digitada de {} e {} é {}".format(n1, n2, resto_da_divisao))
print("A Divisão inteira digitada de {} e {} é {}".format(n1, n2, divisao_inteira))

# Ou

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
resto_da_divisao = n1 % n2
divisao_inteira = n1 // n2
print(f"O Resto da divisão digitada de {n1} e {n2} é {resto_da_divisao}")
print(f"A Divisão inteira digitada de {n1} e {n2} é {divisao_inteira}")

# 

# Peça um número e mostre o seu quadrado e o seu cubo (use **)

n1 = int(input("Digite um número: "))
quadrado = n1 ** 2
cubo = n1 ** 3
print("O quadrado de {} é {} e o cubo é {}".format(n1, quadrado, cubo))

# Ou

n1 = int(input("Digite um número: "))
quadrado = n1 ** 2
cubo = n1 ** 3
print(f"O quadrado de {n1} é {quadrado} e o cubo é {cubo}")

# Nível 2 — Combinando operadores

# Questão 4

# Peça a nota de 3 provas e calcule a média aritmética simples.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
soma = n1 + n2 + n3
quantidade = 3
divisao = soma / quantidade    
print(f"A nota dessa média aritmética simples é")
print(f"Nota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}")
print(f"A sua quantidade é: {quantidade}")
print(f"A divisão de tudo é: {divisao}")

# Outra forma 

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
soma = n1 + n2 + n3
quantidade = 3
media = soma / quantidade
print(f"Nota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}")
print(f"A média aritmética simples é: {media}")

# Outra forma com .format

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
soma = n1 + n2 + n3
quantidade = 3
media = soma / quantidade
print("A nota dessa média aritmética simples é")
print("Nota 1: {}\nNota 2: {}\nNota 3: {}".format(n1, n2, n3))
print("A sua quantidade é: {}".format(quantidade))
print("A divisão de tudo é: {}".format(divisao))

# Peça o preço de um produto e a quantidade comprada; 
# calcule o total, aplicando 10% de desconto se a quantidade
# for maior que 5 (pode usar só aritmética por enquanto
# sem if, supondo quantidade fixa > 5).


