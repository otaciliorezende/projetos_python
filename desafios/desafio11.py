# Escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado 
# Calcule o preço a pagar, sabendo que o carro custa R$80 por dia e R$0,20 por km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 80) + (km * 0.20)
print('O total a pagar é de R${:.2f}'.format(pago))