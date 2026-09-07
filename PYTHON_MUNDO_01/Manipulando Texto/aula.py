# Manipulando Texto

frase = 'Curso em Vídeo Python'
# 21 caracteres e 20 índices de posições 

# Fatiamento de strings
print(frase)  # Curso em Vídeo Python
print(frase[9])  # V

# Outro tipo de fatiamento

print(frase[9:13])  # Víde 
# ele pega do índice 9 até o índice 13, mas não pega o índice 13 então ele pega do 9 até o 12.

# Outro tipo de fatiamento

print(frase[9:21])  # Vídeo Python
# ele pega do índice 9 até o índice 21, mas o 21 não existe então ele pega do 9 até o 20, sem deixar de fora o último índice.

# Outro tipo 

print(frase[9:21:2])  # VdoPto
# ele pega do índice 9 até o índice 21, pulando de 2 em 2, então ele pega o índice 9, pula o 10, pega o 11, pula o 12, pega o 13 e assim por diante.

# Outro tipo 

print(frase[:5])  # Curso
# ele pega do início até o índice 5, mas não pega o índice 5 então ele pega do início até o 4.

# Outro tipo

print(frase[15:])  # Python
# ele pega do índice 15 até o final da string.

# Outro tipo

print(frase[9::3])  # VePh
# ele pega do índice 9 até o final da string, pulando de 3 em 3, então ele pega o índice 9, pula o 10 e o 11, pega o 12, pula o 13 e o 14, pega o 15 e assim por diante.



