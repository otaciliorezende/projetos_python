# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode compra.
#Considerando o US$1,00 = R$5,25.

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.25
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
