#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final a mensagem de acordo com a média atingida:
# REPROVADO: abaixo de 5.0 - RECUPERAÇÃO: entre 5.0 e 6.9 - APROVADO: Superior ou igual à 7.0
from time import sleep

print('='*10)
print('Vamos calcular sua média e ver se já está de férias? ')
print('='*10)
n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
f = (n1+n2)/2
print('Deixe-me calcular seu status.')
sleep(1)
if f<5.0:
    print('Você não conseguiu atingir o mínimo requerido para se formar. Sua média ficou em {:.1f}'.format(f))
elif f>5.0 and f<6.9:
    print('Você ficou de recuperação, mas não se desespere. Com sua média em {:.1f} você ainda pode recuperar'.format(f))
else:
    print('PARABÉNS!! Você se dedicou e está aprovado. Sua média ficou em {:.1f}. Boas férias!!'.format(f))