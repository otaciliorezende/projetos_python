# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
# com 20% de aumento.

salário = float(input('Qaul é o salário do funcionário? R$'))
novo = salário + (salário * 20 / 100)
print('O funcionáro que ganhava R${:.2f}, com 20% de aumento, passa a ganhar {:.2f}'.format(salário, novo))