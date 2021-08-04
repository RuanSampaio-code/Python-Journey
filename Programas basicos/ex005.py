print('==== PROGRAMA PARA DESCOBRIR ANTECESSOR E SUCESSOR DE UM NUMERO ====')

num = int(input('\033[30;7m Digite um número:\033[m'))
anter = num - 1
suces = num + 1
print(' O número \033[1m{}\033[m tem como o antecessor '
      'o numero \033[1m{}\033[m e sucessor o número \033[1;3m{}.'.format(num, anter,suces,))