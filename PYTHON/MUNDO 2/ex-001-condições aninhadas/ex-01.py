#programa para aprovar emprestimo bancario...perguntar valor da casa, salario e em quantos anos ele vai pagar...a prestaçao mensal n pode exceder 30% do salario ou entao sera negada
print("Bem vindo ao consultor de emprestimos!")
valorCasa = float(input("Qual o valor da casa que deseja? R$"))
salario = float(input("Qual o seu salário? R$"))
tempo = int(input("Em quantos anos dejesa pagar? "))
prestacao = valorCasa / (tempo * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de: R${:.2f}" .format(valorCasa, tempo, prestacao))
if prestacao <= minimo:
    print("O seu emprestimo pode ser consedido.")
else:
    print("Seu emprestimo não pode ser aprovado.")

print("-=-" * 25)