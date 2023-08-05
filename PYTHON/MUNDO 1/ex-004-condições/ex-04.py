#programa que le a velocidade de um carro e multa se passar de 80km/h....multa de R$7 por km acima do limite
velocidade = float(input("Digite a sua velocidade: "))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print("Você esta dentro do limite permido!!")
else:
    print("Você ultrapassou o limite e ganhou uma multa de: R${:.2f}" .format(multa))
    