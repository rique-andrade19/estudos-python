#operadores aritmeticos
print(5 + 2) #sinal "+" soma
print(5 - 2) #sinal "-" subtração
print(5 * 2) #sinal "*" multiplicação
print(5 / 2) #sinal "/" divisão
print(5 ** 2) #sinal "**" potencia
print(5 // 2) #sinal "//" divisão inteira, sem números quebrados
print(5 % 2) #sinal "%" resto da divisão
#resto de precedencia
# 1-()
# 2-**
# 3-*, /, //, %
# 4- +, -
n1 = int(input("Seu primeiro número: "))
n2 = int(input("Seu segundo número: "))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
m = n1 * n2
print("A soma é {}, a subtração {}, a divisão {} e a multiplicação {}" .format(s, sub, d, m))
#":.2f" duas casas decimais