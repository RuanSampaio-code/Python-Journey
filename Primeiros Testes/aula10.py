print(' Estrutura condicionais')
print(' aqui tem estruras como '
      'if: essa para blocos verdadeiros'
      'else: essa para bolcos falsos'
      '')

#exemplosnome=
n1 = float(input('Qual a sua primeira nota?'))
n2 = float(input('Qual a sua segunda nota?'))
m = (n1+n2)/2
print(" A sua media foi {:.2f}".format(m))
if m>=7:
    print('Voce foi aprovado!')
else:
    print('Voçe foi reprovado')