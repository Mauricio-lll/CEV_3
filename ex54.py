#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JA SAO MAIORES.
from datetime import date
maior = 0
menor = 0

for c in range(7):
    data = int(input('Em que ano você nasceu? '))
    anos = date.today().year - data
    if anos >= 18:
        maior += 1
    else:
        menor += 1
print('Temos {} pessoas com menos de 18 anos e {} com mais de 18 anos.'.format(menor,maior))