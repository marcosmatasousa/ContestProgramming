def busca_bin(lista, esq, dir, x):
    if dir >= esq:
        m = (dir + esq) // 2
        if lista[m] == x:
            return 1
        elif lista[m] > x:
            return busca_bin(lista, esq, m - 1, x)
        else:
            return busca_bin(lista, m + 1, dir, x)
    else:
        return 0
    
def delRpt(lista):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == lista[i - 1]:
            del lista[i]
    return lista
    

while True:
    a, b = map(int, input().split(" "))
    if a == 0 and b == 0:
        break
    
    ca = delRpt([int(i) for i in input().split(" ")])
    cb = delRpt([int(i) for i in input().split(" ")])
    
    count_a = 0
    count_b = 0
    for i in range(len(ca)):
        if busca_bin(cb, 0, len(cb) - 1, ca[i]) == 0:
            count_a += 1
    for i in range(len(cb)):
        if busca_bin(ca, 0, len(ca) - 1, cb[i]) == 0:
            count_b += 1
    
    print(min(count_a, count_b))