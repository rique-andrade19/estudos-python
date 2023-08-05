#programa que analisa um nome
nome = str(input("Digite seu nome completo: "))#para tirar os espaços
print("Analizando seu nome....")
print("Seu nome em maiúsculas é: {}".format(nome.upper()))
print("Seu nome em minusculas é: {}" .format(nome.lower()))
print("Seu nome tem ao todo {} letras" .format(len(nome) - nome.count(" ")))