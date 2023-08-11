t = int(input())

for _ in range(t):
    n = int(input())
    word = input()
    aux = ""
    fator = 1
    i = 0
    while i < (len(word)):
        if fator == 1:
            aux += word[i]
            fator = 2
            i += 1
        elif fator == 2:
            aux += 2 * word[i]
            fator = 1
            i += 2

    if aux == word:
        print("YES")
    else:
        print("NO")