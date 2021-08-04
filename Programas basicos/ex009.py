print('=====\033[36;5mCONVERSOR DE MOEDA\033[m')
real = float(input("Quanto de real você tem?"))
dolar = real*5.75
print('A quantia de R$ {:.2f} que você tem corresponde a US$ {:.2f} .'.format(real,dolar))