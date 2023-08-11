t = int(input())

for _ in range(t):
    c1, c2, c3 = map(int, input().split(" "))
    a, b, c, d, e = map(int, input().split(" "))

    # jogando A fora
    if a <= c1:
        c1 -= a
        a = 0
    else:
        a -= c1
        c1 -= a

    # jogando B fora
    if b <= c2:
        c2 -= b
        b = 0
    else:
        b -= c2
        c2 -= b  
    
    # jogando c fora
    if c <= c3:
        c3 -= c
        c = 0
    else:
        c -= c3
        c3 -= c

    # jogando D fora em c1
    if d <= c1:
        c1 -= d
        d = 0
    else:
        d -= c1
        c1 -= d
    
    # se sobrou D
    if d > 0:
        if d <= c3:
            c3 -= d
            d = 0
        else:
            d -= c3
            c3 -= d

    if e <= c2:
        c2 -= e
        e = 0
    else:
        e -= c2
        c2 -= e

    # se sobrou E
    if e > 0:
        if e <= c3:
            c3 -= e
            e = 0
        else:
            e -= c3
            c3 -= e

    if a == b == c == d == e == 0:
        print("YES")
    else:
        print("NO")