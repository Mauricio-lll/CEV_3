#usado if / elif e else
nome = str(input('Olá, qual o seu nome? '))
if nome == 'Mauricio':
    print('Seu nome é maravilhoso;')
elif nome in 'Maria Antonia Julia Fernanda':
    print("Seu nome é bem normal sabia?")
print('Seja muito bem vindo ao nosso mundo, {}'.format(nome))
#elif pode ser usado quantas vezes forem necessárias