"""
MÓDULOS EM PYTHON (e a biblioteca math)
Roda o arquivo inteiro no VS Code (▶ ou python modulos.py)
"""

# ============================================================
# 1) O QUE É UM MÓDULO
# ============================================================

# Módulos são arquivos .py que contêm funções, classes e variáveis
# que podem ser reutilizadas em outros programas.


# ============================================================
# 2) FORMAS DE IMPORTAR
# ============================================================

# import bebidas               -> importa TODO o módulo "bebidas"
#                                  (uso: bebidas.refrigerante)
# from bebidas import refrigerante -> importa só o que você precisa
#                                  (uso: refrigerante, direto, sem prefixo)


# ============================================================
# 3) BIBLIOTECA MATH (já vem com o Python, não precisa instalar)
# ============================================================

import math  # importando o módulo inteiro

print("--- FUNÇÕES DO MATH ---")

print(math.ceil(4.3))       # 5  -> ceil()  = arredonda para CIMA
print(math.floor(4.7))      # 4  -> floor() = arredonda para BAIXO
print(math.trunc(4.7))      # 4  -> trunc() = corta a parte decimal (arredonda pra 0)
print(math.pow(2, 3))       # 8.0 -> pow()  = potenciação (sempre retorna float)
print(math.sqrt(16))        # 4.0 -> sqrt() = raiz quadrada
print(math.factorial(5))    # 120 -> factorial() = fatorial (5! = 5*4*3*2*1)


# ============================================================
# 4) IMPORTANDO SÓ UMA FUNÇÃO ESPECÍFICA
# ============================================================

from math import sqrt  # importa só sqrt, sem precisar escrever "math." toda hora

print("\n--- IMPORT ESPECÍFICO ---")
print(sqrt(25))  # 5.0 -> não precisa mais escrever math.sqrt()


# ============================================================
# RESUMO MENTAL
# ============================================================

# ceil     -> pra CIMA
# floor    -> pra BAIXO
# trunc    -> corta decimal, sem arredondar de verdade
# pow      -> potência
# sqrt     -> raiz
# factorial-> fatorial

# import modulo            -> usa modulo.funcao()
# from modulo import funcao -> usa funcao() direto