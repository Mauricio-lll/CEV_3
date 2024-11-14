'''cont = 1
while True: #Executa infinito enquanto não tiver um Break
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')
n = s = 0
while n != 999: #999 seria a Flag, ponto de parada
    n = int(input('Digite um número: '))
    s += n
s -= 999 #Isso só é feito como gambiarra, tirando a flag
print('A soma vale {}'.format(s))'''
n = s = 0
while True: #ponto de parada
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
