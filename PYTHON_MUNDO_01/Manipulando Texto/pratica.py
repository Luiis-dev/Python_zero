"""
Prática de manipulação de texto em Python.
"""

# normalmente
frase = "Curso em vídeo de python"
print(frase) # imprime a frase completa

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[3]) # imprime o caractere no índice 3

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[3:13]) # imprime os caracteres do índice 3 até o índice 12

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[:13]) # imprime os caracteres do início até o índice 12

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[13:]) # imprime os caracteres do índice 13 até o final

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[1:15])  # do índice 1 até o índice 15

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[1:15:2])  # do índice 1 até o índice 15, pulando de 2 em 2

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[1::2])  # do índice 1 ao fim, pulando de 2

# fatiamento de strings
frase = "Curso em vídeo de python"
print(frase[::2])  # do início ao fim, pulando de 2

# extra: 
print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")

# print com """()""" serve para imprimir textos multilinha

# Análise de strings
frase = "Curso em vídeo de python"
print(frase.count("o")) # conta quantas vezes a letra "o" aparece na frase
# O maiúsculo é diferente de o minúsculo

# Análise de strings
frase = "Curso em vídeo de python"
print(frase.upper().count("O")) # conta quantas vezes a letra "o" aparece na frase, ignorando maiúsculas e minúsculas

# 
frase = "Curso em vídeo de python"
print(len(frase)) # conta quantos caracteres tem na frase, incluindo espaços

# 
frase = "Curso em vídeo de python"
frase [0] = "J" # não é possível alterar uma string, pois elas são imutáveis

# 
frase = "Curso em vídeo de python"
frase = frase.replace("python", "Android") # substitui a palavra "python" por "Android"
print(frase) # a frase original não é alterada, pois strings são imutáveis

# Análise de strings
frase = "Curso em vídeo de python"
frase = frase.replace("python", "Android") # substitui a palavra "python" por "Android"
print("Curso" in frase)  # verifica se a palavra "Curso" está na frase

# Análise de strings
frase = "Curso em vídeo de python"
print(frase.find("Curso")) # retorna o índice da primeira ocorrência da palavra "Curso" na frase
# se for retornar -1, significa que a palavra não foi encontrada na frase

# 
frase = "Curso em vídeo de python"
print(frase.lower().find("vídeo"))

# Divisão de strings
frase = "Curso em vídeo de python"
print(frase.split()) # divide a frase em uma lista de palavras, separadas por espaços

# pode fazer
frase = "Curso em vídeo de python"
dividido = frase.split() # divide a frase em uma lista de palavras, separadas
print(dividido[0]) # imprime a primeira palavra da lista

# Divisão de strings
frase = "Curso em vídeo de python"
dividido = frase.split() # divide a frase em uma lista de palavras, separadas
print(dividido[2][3]) # imprime o quarto caractere da terceira palavra da lista
# exemplo: dividido[2] = "vídeo", então dividido[2][3] = "e"

