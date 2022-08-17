digito = input('Digite algo ')
numerico = digito.isnumeric()
alpha = digito.isalpha()
alpha_numerico = digito.isalnum()

print (f'O valor digitado é alfabetico? {alpha}')
print (f'O valor digitado é númerico? {numerico}')
print (f'O valor digitado é alfanúmerico? {alpha_numerico}')
