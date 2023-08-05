#programa que le um angulo e diz seu SENO, COSSENO e TANGENTE
import math
angulo = float(input("Digite seu ângulo: "))
seno = math.sin(math.radians(angulo))
print("O angulo de: {} tem o SENO de: {:.2f}" .format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O COSSENo de: {:.2f}" .format(cosseno))
tangente = math.tan(math.radians(angulo))
print("E a TANGENTE é: {:.2f}" .format(tangente))
