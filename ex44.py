#Elabore um programa que calcula o valor a ser pago por um produto, considerando o seu 'preço normal' e "condição de pagamento":
# à vista (Dinheiro/Cheque): 10% de desconto
# à vista (cartão): 5% de desconto
# Em até 2x (cartão): Preço normal
# 3x ou mais (cartão): 20% juros
print('-'*20)
print('CALCULADORA DE PREÇO ')
print('-'*20)

p = float(input('Qual o preço do produto? '))
f = str(input('A forma de pagamento será Cartão ou Dinheiro? '))
d = float(input('No cartão será em quantas vezes? '))
if f=='Cartão' and d==1:
    print('Pagando em 1x no cartão, seu produto que custava R$ {:.2f} teve um desconto de 5% e agora custa R$ {:.2f}'.format(p,p*1.05))
elif f=='Cartão' and d==2:
    print('Pagamento em 2x no cartão, seu produto que custava R$ {:.2f} manterá o mesmo valor, sem acréscimo de juros. Cada parcela custará R$ {:.2f}.'.format(p,p/d))
elif f=='Cartão' and d>=3:
    print('Pagando em {:.0f}x, seu produto irá ter um juros de 30% para cada parcela, ficando assim um total de R$ {:.2f} e de R$ {:.2f} para cada parcela.'.format(d,p*1.3,(p*1.3)/d))
elif f=='Dinheiro' or f=='Cheque':
    print('O preço do seu produto era R$ {:.2f} e com o pagamento em Dinheiro você recebeu um desconto de 10% e seu novo valor será R$ {:.2f}'.format(p,p/1.1))
