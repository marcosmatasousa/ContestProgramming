while True:
    texto = input()
    if texto == "DONE":
        break
    
    texto = texto.lower()
    texto = texto.replace(',', "")
    texto = texto.replace('.', "")
    texto = texto.replace('!', "")
    texto = texto.replace('?', "")
    texto = texto.replace(" ", "")
    
    if texto == texto[::-1]:
        print("You won't be eaten!")
    else:
        print('Uh oh..')