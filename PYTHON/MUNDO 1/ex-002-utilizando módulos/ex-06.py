#programa que le nomes e sorteia uma ordem 
import random
n1 = input("Digite o primeiro nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)   #para embaralhar a lista
print("A ordem de apresentação sera: ")
print(lista)
#como usamos apenas o "shuffle", podemos importar assim: from randon import shuffle