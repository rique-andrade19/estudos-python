#programa que le um numero inteiro e pede para o usuario escolher se quer converter para binario, octal ou hexadecimal
num = int(input("Digite um número inteiro: "))
print("Escolha uma opção para converter")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} concertido para BINÀRIO é: {}" .format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é: {}" .format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é: {}" .format(num, hex(num)[2:]))
else: 
    print("OPÇÃO INVALIDA!!!")