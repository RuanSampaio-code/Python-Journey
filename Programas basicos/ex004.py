
n = input('Digite algo: ')
print('O tipo primitivo desse valor é \033[1;30;41m{} \033[m'.format(type(n)))
print('Só tem espaços? \033[1;30;41m{}\033[m'.format(n.isspace()))
print('É um número? \033[1;30;41m{}\033[m'.format(n.isnumeric()))
print('É alfabético? \033[1;30;41m{}\033[m'.format(n.isalpha()))
print('É alfanúmerico? \033[1;30;41m{}\033[m'.format(n.isalnum()))
print('Está em maiúsculas? \033[1;30;41m{}\033[m'.format(n.isupper()))
print('Está em minúsculas? \033[1;30;41m{}\033[m'.format(n.islower()))
print('Está capitalizado? \033[1;30;41m{}\033[m'.format(n.istitle()))

