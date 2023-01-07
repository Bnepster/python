# Criando uma calculadora

# Valores que serão manipulados
a = float(input('Digite um número '))
b = float(input('Digite outro número '))

# Operações aritméticas
adiçao = a + b
subtraçao = a - b

# Escolhendo qual operador usar
c = input('Deseja somar ou subtrair ')

# Condição para qual operador foi escolhido
if c == 'somar':
    print(adiçao)
else:
    print(subtraçao)

# Fim do programa
print('O programa foi executado com sucesso')

