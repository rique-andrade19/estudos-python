#programa que le valor em metros e exibe em cm e mm
metros = float(input("Digite quantos metros: "))
cm = metros * 100
mm = metros * 1000
print("Você escolheu: {} metros, sua medida em cm é: {} e em mm é: {}" .format(metros, cm, mm))