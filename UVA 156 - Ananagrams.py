texto = input()
while True:
    aux = input()
    if aux == '#':
        break
    texto = texto + (" " + aux)
    
texto = list(texto.split(" "))

anana = []
for i in range(len(texto)):
    count = 0
    textoA = sorted(texto[i].lower())
    for j in range(len(texto)):
        if i != j:
            if textoA == sorted(texto[j].lower()):
                count += 1
    if count == 0:
        anana.append(texto[i])

anana.sort()
for i in range(len(anana)):
    print(anana[i])