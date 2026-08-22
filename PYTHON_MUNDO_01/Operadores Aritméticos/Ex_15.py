# Exercicio 15

# "Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por km rodado."

km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias alugados: "))
km_custo = km * 0.15
dias_custo = dias * 60
total = km_custo + dias_custo
print("O total a pagar é: R${:.2f}".format(total))
print("Detalhes do cálculo: \nCusto por km: R${:.2f} \nCusto por dias: R${:.2f}".format(km_custo, dias_custo))

# Resposta do Guanabara:

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar é R${:.2f}".format(pago))


