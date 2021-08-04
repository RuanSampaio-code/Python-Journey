print('=====Dobro triplo e raiz=====')
n = float(input('Digite um numero: '))
dobro = 2*n
triplo = 3*n
raiz = pow(n, 1/2)
print('O dobro de \033[1;32m{}\033[m é \033[1;32m{}\033[m.'.format(n,dobro))
print('Seu triplo é \033[3;32m{}\033[m e sua raiz quadrada é \033[3;32m{:.2f}\033[m.'.format(triplo, raiz))