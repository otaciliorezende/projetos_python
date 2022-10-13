# Faça um algoritmo que leia preço do produto e mostre seu nomo preço,
# com 5% de desconto.

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 8 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 8% vai custar R${:.2f}'.format(preço, novo))