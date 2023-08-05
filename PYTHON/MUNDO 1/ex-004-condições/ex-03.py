#jogo de adivinhação
from random import randint
num = randint(0, 5) #faz o computador sortear um número
print("-=-" * 10)
print("EU PENSEI EM UM NUMERO ENTRE 1 e 5, TENTE ACERTAR")
jogador = int(input("Em que número eu pensei? "))
if jogador == num:
    print("PARABENS!!")
else:
    print("Eu pensei em {} e não em {}" .format(num, jogador))