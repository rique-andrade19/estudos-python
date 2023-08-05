# #programa que le o lado oposto e adjacente de um triangulo retangulo e mostra a hipotenusa
# co = float(input("Digite o comprimento do cateto oposto: "))
# ca = float(input("Digite o comprimento do cateto adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print("A hipotenusa vai medir: {:.2f}" .format(hi))

#agora importando bibliotecas
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A sua hipotenusa vai medir: {:.2f}". format(hi))
#math.hypot é o calculo da hipotenusa