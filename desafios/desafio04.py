# Conversor de Medidas
# Escreva um programa que leia um valor em metros e o exiba
#convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A medida de {}m \n corresponde a {}cm \n {}mm \n {:.2f}dam \n {}hm \n {}km'.format(medida, cm, mm, dam, hm, km))