t = int(input())

for _ in range(t):
    n = int(input())
    text = input()
    balanco = 0
    count = 0
    
    for i in range(len(text)):
        if text[i] == "(":
            balanco += 1
        else:
            balanco -=1
            if balanco < 0:
                balanco = 0
                count += 1

    print(count)