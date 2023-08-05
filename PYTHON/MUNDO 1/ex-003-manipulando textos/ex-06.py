#programa que le o nome de uma pessoa e mostra seu primeiro e ultimo nome separadamente
n = str(input("Digite seu nome completo: ")) .strip()
nome = n.split()
print("Seu primeiro nome é: {}" .format(nome[0]))
print("Seu ultimo nome é: {}" .format(nome[len(nome) - 1]))