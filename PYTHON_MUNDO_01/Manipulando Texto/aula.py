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



# Análise de strings

print(len(frase))  
# len vem de length, que significa comprimento, então ele vai contar quantos caracteres tem na string, incluindo os espaços. O resultado é 21.

# Outra forma de análise de strings

print(frase.count('o'))
# count vem de contar, então ele vai contar quantas vezes o caractere 'o' aparece na string. O resultado é 3.

# Outra forma de análise de strings
print(frase.count('o', 0, 13))
# contagem com fatiamento, então ele vai contar quantas vezes o caractere 'o' aparece na string, mas só vai contar do índice 0 até o índice 13, então o resultado é 1.

# Outra forma de análise de strings

print(frase.find('deo'))
# find vem de encontrar, então ele vai encontrar o índice do início da string 'deo' na string 'Curso em Vídeo Python'. O resultado é 11.

# Outra forma de análise de strings

print(frase.find('Android'))
# se não encontrar a string, ele vai retornar -1, então o resultado é -1.

# Outra forma de análise de strings

print('Curso' in frase)
# in vem de dentro, então ele vai verificar se a string 'Curso' está dentro da string 'Curso em Vídeo Python'. O resultado é True.

# Transformação de strings

print(frase.replace('Python', 'Android'))
# replace vem de substituir, então ele vai substituir a string 'Python' pela string 'Android' na string 'Curso em Vídeo Python'. O resultado é 'Curso em Vídeo Android'.

# Outra forma de transformação de strings

print(frase.upper())
# upper vem de maiúsculo, então ele vai transformar todos os caracteres da string 'Curso
    # em Vídeo Python' em maiúsculo. O resultado é 'CURSO EM VÍDEO PYTHON'.

# Outra forma de transformação de strings

print(frase.lower())
# lower vem de minúsculo, então ele vai transformar todos os caracteres da string 'Curso
    # em Vídeo Python' em minúsculo. O resultado é 'curso em vídeo python'.

# Outra forma de transformação de strings

print(frase.capitalize())
# capitalize vem de capitalizar, então ele vai transformar o primeiro caractere da string 'Curso em Vídeo Python' em maiúsculo e os demais caracteres em minúsculo. O resultado é 'Curso em vídeo python'.

# Outra forma de transformação de strings

print(frase.title())
# title vem de título, então ele vai transformar o primeiro caractere de cada palavra da string

# Outra forma de transformação de strings: Com a string ' Aprenda Python'.

print(frase.strip())
# strip vem de remover, então ele vai remover os espaços em branco do início e do final

# Outra forma de transformação de strings

print(frase.rstrip())
# rstrip vem de remover à direita, então ele vai remover os espaços em branco do final da string 'Curso em Vídeo Python'.

# Outra forma de transformação de strings

print(frase.lstrip())
# lstrip vem de remover à esquerda, então ele vai remover os espaços em branco do início

