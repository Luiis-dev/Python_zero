# Exercicio 13

# "Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salária, com 15% de aumento."

salario = float(input("Digite seu salário: "))
novo_salario = salario + (salario * 0.15 / 100)
print("Salário era {} e agora com aumento de 15% vai ficar {}".format(salario, novo_salario))

# Resposta do Guanabara

salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))



