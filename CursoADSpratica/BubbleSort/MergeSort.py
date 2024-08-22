def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


ll = [56, 76, 12, 2, 5, 87, 23, 1, 67, 13]
print(mergesort(ll))
