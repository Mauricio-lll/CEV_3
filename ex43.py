#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela:
# Abaixo do peso - Abaixo de 18.5
# Peso Ideal - Entre 18.5 e 25
# Sobrepeso - De 26 até 30
# Obesidade - De 31 até 40
# Obesidade Mórbida - Acima de 40:
# IMC = Massa (kg) ÷ Altura (m)**
print('-'*20)
print('VAMOS CALCULAR SEU IMC?')
print('-'*20)
p = float(input('Qual seu peso em kg? '))
a = float(input('Qual sua altura em m? '))
IMC = p/((a**2))
if IMC<=18.5:
    print('Seu IMC é de {:.2f} e com isso você se encontra Abaixo do peso.'.format(IMC))
elif IMC>18.5 and IMC<=25:
    print('Seu IMC é de {:.2f} e com isso você está no seu peso ideal, parabéns.'.format(IMC))
elif IMC>25 and IMC<=30:
    print('Cuidado, você chegou na fase de sobrepeso. Com o IMC de {:.2f} você deve começar a cuidar da sua alimentação.'.format(IMC))
elif IMC>30 and IMC<=40:
    print('CUIDADO!! Você chegou na fase de Obesidade. Pedimos que busque a ajuda médica para que isso não afete ainda mais sua saude. Com o IMC de {:.2f} qualquer kg é um risco'.format(IMC))
else:
    print('SEU IMC É DE {:.2f}. CONTATE UM MÉDICO O QUANTO ANTES, SUA SAUDE NÃO É BRINCADEIRA'.format(IMC))