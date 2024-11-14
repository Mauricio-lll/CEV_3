# Faça um programa que leia o sexo da uma pessoa, mas só aceite valores "M" e "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

while sexo not in 'MF': #Aqui pode deixar o sexo junto, por serem duas letras, mas colocar o not in
    print('Valor inválido. Preencha com F para feminino e M para masculino.')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
print(f'Sexo registrado com sucesso: {sexo}')

