# para mostrar apenas a parte inteira do número usamos math.trunc
from math import trunc
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é {}" .format(num, trunc(num)))

#sem importar nenhuma biblioteca
num = float(input("Digite um valor: "))
print("O valor digitado foi: {}, e sua parte inteira é {}" .format(num, int(num)))