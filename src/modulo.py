def func(pedras="", joia=""):
    # Escreva seu codigo aqui
    np = 0
    pedras_set = set(pedras)
    for p in pedras_set:
        for j in joia:
            if p == j:
                np +=1
    return np