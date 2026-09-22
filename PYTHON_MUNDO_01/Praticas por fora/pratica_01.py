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

# Questão 3

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

# Peça a nota de 3 provas e calcule a média aritmética simples.

