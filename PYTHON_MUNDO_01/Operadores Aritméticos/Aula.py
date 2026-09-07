"""OPERADORES ARITMÉTICOS EM PYTHON"""

# ============================================================
# 1) OS OPERADORES
# ============================================================

print("--- OPERADORES ---")
print("+  = Adição")
print("-  = Subtração")
print("*  = Multiplicação")
print("/  = Divisão")
print("// = Divisão inteira")
print("%  = Resto da divisão")
print("** = Exponenciação, potenciação")


# ============================================================
# 2) ORDEM DE PRECEDÊNCIA (do que é calculado primeiro pro último)
# ============================================================

print("\n--- PRECEDÊNCIA ---")
print("1. ()")
print("2. **")
print("3. * / // %")
print("4. + -")


# ============================================================
# 3) ENTRADA DE DADOS
# ============================================================

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))


# ============================================================
# 4) CÁLCULOS
# ============================================================

s = n1 + n2      # soma  (era "s = n1 = n2" -> corrigido pra "+")
m = n1 * n2      # multiplicação
d = n1 / n2      # divisão (float)
di = n1 // n2    # divisão inteira
r = n1 % n2      # resto da divisão
e = n1 ** n2     # potenciação


# ============================================================
# 5) RESULTADOS
# ============================================================

print("\n--- RESULTADOS ---")

# {:.3f} = arredonda pra 3 casas decimais
print("a soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d))

# faltava um {} pra mostrar a potência (e) -> corrigido abaixo
print("divisão inteira {}, resto da divisão {} e potência {}".format(di, r, e))


# Lembretes rápidos:
# end=" "  -> evita quebrar a linha no print
# \n       -> força quebra de linha dentro da string