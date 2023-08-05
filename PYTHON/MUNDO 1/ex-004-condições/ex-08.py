#programa que le 3 numero e mostra qual o maior e o menor
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
print("_" * 20)
menor = n1 
#verifica quem é o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verifica quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 >  n1 and n3 > n2:
    maior = n3
print("O menor valor digitado foi: {}" .format(menor))
print("O maior valor digitado foi: {}" .format(maior))