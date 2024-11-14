#Crie um programa que leia uma frase e diga se ela é um Palindromo, desconsidere os espaços
frase = input('Digite sua frase: ').upper()
espaco = frase.replace(" ","")
retorno = espaco[::-1]
if retorno == espaco:
    print('Sua frase é um PALINDROMO: {}'.format(retorno))
else:
    print('Não conseguimos formar um PALINDROMO: {}'.format(retorno))
