# 1 Exercicio 
soma_do_numero = int(input("Digite Um Número: "))
soma_do_segundo_numero = int(input("Digite Outro Número: "))
soma = soma_do_numero + soma_do_segundo_numero
print("A Soma de {} e {} é igual a {}".format(soma_do_numero, soma_do_segundo_numero, soma))

# Exemplos e praticas do exercicio
# float
soma_do_numero = float(input("Digite Um Número: "))
soma_do_segundo_numero = float(input("Digite Outro Número: "))
soma = soma_do_numero + soma_do_segundo_numero
print("A soma de {} e {} é igual a {}".format(soma_do_numero, soma_do_segundo_numero, soma))

# string
nome = str(input("Digite Um Nome: "))
segundo_nome = str(input("Digite Outro Nome: "))
nome_completo = nome + " " + segundo_nome
print("seu nome é {} e seu sobrenome e {} juntos são {}".format(nome, segundo_nome, nome_completo))

# booleano
e_verdadeiro = bool(input("Digite Um Valor Booleano: "))
print("O valor booleano digitado é {}".format(e_verdadeiro))


# 2 Exercicio
nome = str(input('Digite Algo: '))
print(type(nome))
print(nome.isnumeric())  # se e possivel converter para numero
print(nome.isalpha())  # se ele e letra
print(nome.isalnum())  # se ele e alfanumérico
print(nome.isupper())  # se ele está somente com letras maiúsculas
print(nome.islower())  # se ele está somente com letras minúsculas
print('Só tem espaço?', nome.isspace())  # se ele é só espaço
print('Está capitalizada?', nome.istitle())  # se ele está capintalizado