# Exercicio 12

#"Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto."

produto = float(input("Digite o valor do produto: "))
novo_preco = produto - (produto * 0.05 / 100)
print("O produto valia {} e com desconto de 5% vai ficar em  {}".format(produto, novo_preco))

# Resposta do Guanabara

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))

# calculando o desconto de outra forma
preco = float(input('Qual é o preço do produto? R$ '))  
desconto = preco - (preco * 0.95)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))
