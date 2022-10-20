# Faça um programa que leia um ângulo 
# qualquer e mostre na tela o valor do seno,
# coseno e tangente desse ângulo.

import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângolo de {} tem o COSSENO {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('A tangente de {} tem a TANGENTE {:.2f}'.format(ângulo, tangente))
