print("Ok! Agora eu vou mostrar o seu valor com um desconto de 5%!")
valor = float(input("Digite aqui o teu valor: "))
porcentagem = valor*0.05
print("O teu valor com o desconto será de R$ \033[32m{:.2f} reais\033[m".format(valor-porcentagem))


