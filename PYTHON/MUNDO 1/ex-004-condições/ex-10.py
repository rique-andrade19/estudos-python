#programa que le 3 comprimentos e verifica se podem formar um triangulo
print("-=-" * 20)
print()
c1 = float(input("Digite o primeiro segmento: "))
c2 = float(input("Digite o segundo segmento: "))
c3 = float(input("Digite o terceiro segmento: "))
print("-=-" * 20)
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print("Seus segmentos FORMAM um triângulo")
else:
    print("Seus segmentos NÃO FORMAM um triângulo")