#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais (a=b=c)
# Isósceles: Dois lados iguais (a=b=/=c or a=c=/=b or b=c=/a)
# Escaleno: Todos os lados diferentes (a=/=b=/=c)
#Para formar um triangulo, a soma de 2 lados não pode ser INFERIOR ao valor do terceiro lado (a+b>=c)
from time import sleep

print('-'*20)
print('QUAL SERÁ O TIPO DE TRIÂNGULO??')
print('-'*20)
print('*LEMBRANDO QUE PARA SER UM TRIÂNGULO, A SOMA DE 2 LADOS NÃO PODE SER SUPERIOR AO VALOR DO TERCEIRO LADO, OK?')
l1 = float(input('Qual sua primeira reta? '))
l2 = float(input('E sua segunda? '))
l3 = float(input('Qual será sua ultima reta? '))
print('Calculando...')
sleep(1)
if (l1+l2)<l3 or (l1+l3)<l2 or (l2+l3)<l1:
    print('Com esses comprimentos você não consegue formar uma reta, pois a soma de dois lados é superir ao terceiro lado.')
elif l1==l2==l3:
    print('Parece que você formou um triângulo Equilátero, com todos os lados medindo {}'.format(l1))
elif l1==l2 or l2==l3 or l3==l1:
    print('Muito bem, dois lado iguais. Você formou um triângulo Isósceles.')
else:
    print('Nenhum comprimento é igual, isso é um triângulo Escaleno.')
