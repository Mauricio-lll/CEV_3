#A confederação de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade.
# MIRIM - Até 9 anos
# INFANTIL - de 10-14 anos
# JUNIOR - de 15-19 Anos
# SÊNIOR - 20 Anos
# MASTER - 21+
from datetime import date
from time import sleep

print('-'*20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-'*20)
n = int(input('Qual seu ano de nascimento? '))
print('Vamos ver qual será sua categoria para as provas deste ano? ')
sleep(1)
n1 = (date.today().year-n)
if n1 <=9:
    print('Com {} anos você está na categoria MIRIM.'.format(n1))
elif n1>9 and n1<=14:
    print('Com {} anos você está agora na categoria INFANTIL'.format(n1))
elif n1>14 and n1<=19:
    print('Parece que você já está crescendo, sua categoria mudou para JUNIOR, com {} anos'.format(n1))
elif n1==20:
    print('Com {} anos, você se enquadra na categoria SÊNIOR.'.format(n1))
else:
    print('Você já está velho, com {} anos. Mudamos você para a categoria MASTER!'.format(n1))