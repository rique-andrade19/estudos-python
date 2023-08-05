# #programa que diz dobro, triplo e raiz quadrada
# num = int(input("Digite um número: "))
# d = num * 2
# t = num * 3
# r = num ** (1/2)
# print("Seu número é: {}, o dobro é: {}, o triplo: {} e a raiz quadrada: {:.3f}" .format(num, d, t, r))


# #programa que mostra a área de um local e usar 1 litro de tinta por m2
# altura = float(input("Digite a altura: "))
# largura = float(input("Digite a largura: "))
# area = altura * largura
# print("Sua área é de: {}m²" .format(area))
# tinta = area / 2
# print("Para pintar essa parede você precisará de {} litros de tinta".format(tinta))

# #programa que adiciona descontos
preco = float(input("Digite o preço: R$"))
desconto = float(input("Digite o desconto, ex: 50: "))
novo = preco - (preco * desconto / 100)
print("Seu preço era de: R${:.2f}, com o desconto ficou R${:.2f}".format(preco, novo))