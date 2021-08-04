print('=====\033[34;1mConversor de unidade de medida e comprimento\033[m===')
m = float(input('Quantos metros você quer converter?'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print ('{} metros... Convertidos em: '
       '\nMilímetros é igual a {}\nCentímetros é igual a {}'
       '\nDecímetros é igual a {}\nDecâmetros é igual a {}'
       '\nHectômetros é igual a {}\nQuilômetros é igual a {}.'.format(m, mm, cm, dm, dam, hm, km))


