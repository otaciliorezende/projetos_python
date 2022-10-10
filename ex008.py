# Esse código está fechado para todas as possibilidades, e o
# else será executado somente se o usuario final digitar algo
# diferente de 'SIM ou 'NÃO.
nome = input('Digite o nome:')
idade = int(input('Digite a idade:'))
doenca_infectocontagiosa = input('suspeita de doença infectocontagiosa?').upper()
if idade>= 65 and doenca_infectocontagiosa == 'Sim':
    print('O paciente será direcionado para sala AMARELA - COM prioridade')
elif idade < 65 and doenca_infectocontagiosa == 'SIm':
    print('O paciente será direcionado para sala AMRELA SEM prioridade')
elif idade >= 65 and doenca_infectocontagiosa == 'NÃO':
    print('O paciente será direcionado para sala BRANCA - COM prioridade')
elif idade < 65 and doenca-infectocontagiosa == 'NÃO':
    print('O paciente será direcionado para a sela BRANCA - SEM prioridade')
else: 
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')                
