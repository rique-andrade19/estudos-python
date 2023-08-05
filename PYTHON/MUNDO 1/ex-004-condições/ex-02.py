#verificador de média
nome = input("Qual o seu nome? ")
n1 = float(input("Sua primeira nota: "))
n2 = float(input("Sua segunda nota: "))
n3 = float(input("Sua terceira nota: "))
n4 = float(input("Sua quarta nota: "))
pontos = n1 + n2 + n3 + n4
media = (n1 + n2 + n3 + n4) / 4
print("Seus pontos são: {} e sua média é: {:.1f}" .format(pontos, media))
if media >= 6:
    print("Parabens, você esta aprovado")
else:
    print("Você precisa estudar mais!!!") 