#programa que pergunta a distanciq de uma viagem em km. R$0.50 por km para viagens até 200 km e R$0.45 para viagens acima
km = float(input("Qual a distancia de sua viagem? "))
if km <= 200:
    preco = km * 0.50
    print("Sua viagem de {}km vai custar R${:.2f}" .format(km, preco))
else:
    preco = km * 0.45
    print("Sua viagem de {}km vai custar R${:.2f}" .format(km, preco))
    