#programa que le um num inteiro e diz se é par ou impar
num = int(input("Me diga um número qualquer: "))
resultado = num % 2
if resultado == 0:
    print("O número {} é PAR" .format(num))
else:
    print("O número {} é IMPAR" .format(num))