#programa que cobra R$60 por dia e R$0.15 por km rodado
print("R$60 diaria")
print("R$0.15")
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
aluguel = (dias * 60) + (km * 0.15)
print("O valor a ser pago é de: R${:.2f}" . format(aluguel))