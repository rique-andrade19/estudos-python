#programa que le um salário e da aumento...superior a 1250 = 10% e inferior = 15%
salario = float(input("Digite seu salário atual: R$"))
#calculando 10%
if salario > 1250:
    novo = salario + (salario * 0.10)
    print("Seu salário foi de R${:.2f} para {:.2f}" .format(salario, novo))
if salario <= 1250:
    novo = salario + (salario * 0.15)
    print("Seu salário foi de R${:.2f} para R${:.2f}" .format(salario, novo))