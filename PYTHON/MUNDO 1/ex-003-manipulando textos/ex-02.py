#programa que analisa números entre 1000 e 9999
num = int(input("Digite seu número entre 1000 e 9999: "))
n = str(num)
print("Analisando o numero {}" .format(num))
print("Unidade: {}" .format(n[3]))
print("Dezenas: {}" .format(n[2]))
print("Centena: {}" .format(n[1]))
print("Milhar: {}" .format(n[0]))

# ou podemos fazer assim que faz do 0 até 9999
num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 
print("Unidade: {}" .format(u))
print("Dezena: {}" .format(d))
print("Centena: {}" .format(c))
print("Milhar: {}" .format(m))
