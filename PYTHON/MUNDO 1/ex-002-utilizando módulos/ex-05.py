#programa para sorteio de algo da lista
import random
n1 = input("Primeiro nome: ")
n2 = input("Segundo nome: ")
n3 = input("Terceiro nome: ")
n4 = input("Quarto nome: ")
lista = [n1, n2, n3, n4]   #para python uma lista fica entre colchetes
escolhido = random.choice(lista) #randon.choice escolhe um item aleatorio da lista
print("O aluno escolhido foi: {}" .format(escolhido))