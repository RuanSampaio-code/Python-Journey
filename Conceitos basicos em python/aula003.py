print('Manipulando cadeias de textos ou caracteres')

print('Operações de manipulação de textos')
print('1º FATIAMENTO:')

frase ='curso em video python'
print(frase[9])
print( frase[:6])
print(frase[9:14])
print(frase[6:22:2]) # aqui aparecerá caracteres pulando de 2 em 2.
print(frase[4:])
print(frase[9::])
print(frase[9::3])

print('2º ANÁLISE:')
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,15))
print(frase.find('deo'))
print(frase.find("android"))
print('curso' in frase)

print('TRANSFORMAÇÃO')
print(frase.replace('python','android'))
print(frase.upper())
print(frase.lower())# tudo fica minusculo
print(frase.capitalize()) # deica a primeira letra em maiuscula
print(frase.title()) #a primeira letra de cada palavra da string vai ficar em maiusculo
frase2 = '   aprenda python  '
print(frase2)
print(frase2.strip()) #tira os excessos dos espaços do lado


print('DIVISÃO')
print(frase.split()) #divição na string ultilizando os espaços
print('JUNÇÃO')
print('-'.join(frase))    