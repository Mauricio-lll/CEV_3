# Inicializando as variáveis
soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

# Leitura dos dados de 4 pessoas
for pessoa in range(1, 5):
    nome = str(input(f'Digite o nome da pessoa: ')).strip()
    idade = int(input(f'Digite a idade da pessoa: '))
    sexo = str(input(f'Digite o sexo da pessoa (M/F): ')).strip().upper()

    soma_idades += idade

    # Verificando o homem mais velho
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    # Contando mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calculando a média de idade
media_idade = soma_idades / 4

# Imprimindo os resultados
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
if homem_mais_velho:
    print(f'O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos.')