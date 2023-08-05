#faça um programa que leia um salário e de um aumento de 15% 
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário atual: R$"))
aumento = salario + (salario * 15 / 100)
print("Seu salário era R${:.2f} e ficou R${:.2f} depois do aumento.".format(salario, aumento))