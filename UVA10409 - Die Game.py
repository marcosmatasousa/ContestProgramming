while True:

    cima = 1
    norte = 2
    sul = 5
    oeste = 3
    leste = 4
    baixo = 6
    
    n = int(input())
    if n == 0:
        break
    
    for i in range(n):
        jogada = input()
        
        cimaAux = cima
        norteAux = norte
        sulAux = sul
        oesteAux = oeste
        lesteAux = leste
        baixoAux = baixo
        
        if jogada == "north":
            cima = sulAux
            norte = cimaAux
            baixo = norteAux
            sul = baixoAux
            
        elif jogada == "south":
            cima = norteAux
            norte = baixoAux
            baixo = sulAux
            sul = cimaAux
            
        elif jogada == "west":
            cima = lesteAux
            oeste = cimaAux
            leste = baixoAux
            baixo = oesteAux
            
        elif jogada == "east":
            cima = oesteAux
            baixo = lesteAux
            oeste = baixoAux
            leste = cimaAux
            
    print(cima)