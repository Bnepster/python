# Criando um verificador de idade

idade = float(input('Qual a sua idade? -> '))
if idade < 18:
    print('Você é menor de idade')
elif idade >= 65:
    print('Você é um idoso')
else:
    print('Maior de idade')