# Escreva um programa que converta a temperatura digitada
# em °C e converta para °F. 

c = float(input('Informe a temperatura em °C: ')) 
f = ((9 * c) / 5) + 32
print('A temperatura de  {}°C corresponde a  {}°F!'.format(c, f))