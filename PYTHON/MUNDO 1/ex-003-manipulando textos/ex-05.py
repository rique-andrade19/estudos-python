#programa que le uma frase e mostra infos sobre ela 
frase = str(input("Digite sua frase: ")).upper() .strip()
print("A letra A aparece {} vezes na sua frase" .format(frase.count("A")))
print("A primeira letra A aparece na posição: {}" .format(frase.find("A") + 1 ))
print("A posição em que a letra A aparece a ultima vez é: {}" .format(frase.rfind("A") + 1))