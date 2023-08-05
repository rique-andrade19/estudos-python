#programa que le nome de uma cidade e diz se ela começa ou não com "santo".
cidade = str(input("Em que cidade você nasceu? ")).strip()
print(cidade[:5].upper() == "SANTO")  