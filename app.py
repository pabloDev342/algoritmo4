def permutaciones(lista):

    if len(lista) <= 1:
        return [lista]
    
    resultado = []

    for i in range (len(lista)):

        elemento = lista[i]

        resto = lista[:i] + lista[i+1:]

        for perm in permutaciones (resto):
            resultado.append([elemento] + perm)

    return resultado
print(permutaciones([1,2,3,]))