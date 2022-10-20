# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de u  triângulo e mostre o comprimento
# da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))