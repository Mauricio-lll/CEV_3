# Crie um programa que faça o computador jogar Jokenpô:
# Pedra, Papel e Tesoura
# Pedra: Amassa tesoura.
# Papel: Embrulha pedra.
# Tesoura: Corta papel.
import random
print('-'*20)
print('VAMOS BRINCAR DE JOKENPÔ??')
print('-'*20)
print()
c = input('Vamos lá, escolha a sua jogada, Pedra, Papel ou Tesoura? ')
op = ['Pedra', 'Papel', 'Tesoura']
d = random.choice(op)
if c=='Tesoura' and d=='Tesoura'or c=='Pedra' and d=='Pedra' or c=='Papel' and d=='Papel':
    print('Você escolheu {} e eu escolhi {}, parece que empatamos.'.format(c,d))
elif c=='Tesoura'and d=='Papel' or c=='Papel' and d=='Pedra' or c=='Pedra' and d=='Tesoura':
    print('Sua escolha de {} foi sábia. Eu escolhi {} e acabei perdendo essa rodada.'.format(c,d))
elif c=='Tesoura' and d=='Pedra' or c=='Papel' and d=='Tesoura' or c=='Pedra' and d=='Papel':
    print('Sua escolha de {} não foi tão boa. Eu escolhi {} e me dei bem nessa. Mais sorte na próxima.'.format(c,d))
