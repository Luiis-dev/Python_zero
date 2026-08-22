 # Operadores Aritméticos
print("+  = Adição")
print("-  = Subtração")
print("*  = Multiplicação")
print("/  = Divisão")
print("// = Divisão inteira")
print("%  = Resto da divisão")
print("** = Exponenciação, potenciação")

# Ordem de precedência dos operadores aritméticos:
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 = n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2 
e = n1 ** n2
print("a soma é {}, o prduto é {} e a divisão é {:.3f}".format(s, m, d,))

# :.3f = 3 casas decimais
# end= " " = para não quebrar a linha
# \n = quebra de linha

print("divisão inteira {} e Resto da divsão e potência {}".format(di, r, e))


