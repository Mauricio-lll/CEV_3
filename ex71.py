print('=' * 40)
print(f'{"Banco coisa e tal":^40}')
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 40)
print(f'{"Operação finalizada. Tenha um bom dia!":^40}')