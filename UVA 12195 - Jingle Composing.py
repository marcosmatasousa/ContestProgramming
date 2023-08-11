while True:
    music = input()
    if music == '*':
        break
    count = 0
    measure = 0
    
    for i in range(1, len(music)):
        if music[i] == '/':
            if measure == 1:
                count += 1
            measure = 0
        elif music[i] == 'W':
            measure += 1
        elif music[i] == 'H':
            measure += 1/2
        elif music[i] == 'Q':
            measure += 1/4
        elif music[i] == 'E':
            measure += 1/8
        elif music[i] == 'S':
            measure += 1/16
        elif music[i] == 'T':
            measure += 1/32
        elif music[i] == 'X':
            measure += 1/64
    print(count)