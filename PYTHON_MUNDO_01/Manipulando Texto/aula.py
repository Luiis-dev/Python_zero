"""MANIPULAÇÃO DE STRINGS EM PYTHON"""

frase = 'Curso em Vídeo Python'
# 21 Caracteres, índices de 0 a 20


# ==============================================================\
# 1) FATIAMENTO (SLINCING) -> frase[inicio:fim:passo]
#   fim NUNCA é incluido no resultado
# ==============================================================

print("--- FATIAMENTO ---")

print(frase[9])          # V              -> só o caractere no índice 9
print(frase[9:13])       # Víde           -> do 9 até o 12 (13 fica de fora)
print(frase[9:21])       # Vídeo Python   -> do 9 até o fim (21 não existe  -> vai até 20)
print(frase[9:21:2])     # VdoPto         -> do 9 ao 21, pulando de 2 em 2
print(frase[:5])         # Curso          -> do inicio até o indice 4
print(frase[15:])        # Python         -> do índice 15 até o final
print(frase[9::3])       # VePh           -> do 9 até o final, pulando de 3 em 3

# ==============================================================
# 2) ANÁLISE DE STRINGS -> perguntas sobre a string (não altera nada)
# ==============================================================

print("\n--- ANÁLISE ---")

print(len(frase))                # 21     -> quantidade de caracteres (com espaças)
print(frase.count('o'))          # 3      -> quantas vezes 'o' aparece
print(frase.count('o', 0, 13))   # 1      -> conta 'o' só dentro do trecho [0:13]
print(frase.find('deo'))         # 11     -> índice onde 'deo' começa
print(frase.find('Android'))     # -1     -> não encontrou
print('Curso' in frase)          # True   -> 'Curso' está contido na frase ?

# ==============================================================
# 3) DIVISÃO E UNIÃO -> trocar entre string <-> lista
# ==============================================================

print("\n--- DIVISÃO E UNIÃO ---")

print(frase.split())           # ['Curso', 'em', 'Vídeo', 'Python']   -> String vira lista 
print('-'.join(frase))         # C-u-r-s-o-...                        -> lista/string vira string com separador
# atenção: join é chamado a partir do SEPARADOR, não da string original
