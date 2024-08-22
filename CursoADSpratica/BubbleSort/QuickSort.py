# implementação do quick sort
# utiliza o pivot como o ultimo elemnto da lista de númeoros
# tem um ponteiro para manter a localizaçao dos elementos menores que o pivot
# no fim da particion() function, o ponteiro é trocado com o pivot
# volta com um numero sorteado, que tenha alguma relação com o pivot

# função para achar a posição da partição
def partition(array, low, high):
    # escolhe o melhor elemento para pivot
    pivot = array[high]
    # ponteiro para o maior elemento
    i = low - 1
    # passa por todos os elementos
    # compara cada um deles com o pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # se um elemento é menor que o pivot foi encontrado
            # troca o maior elemento com o elemento i
            i += 1

            # troca o elemento em i com o elemento em j
            (array[i], array[j]) = (array[j], array[i])

    # toca o pivo como maior elemento contido em i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # retorna a posição de onde a partiçãoa acaba
    return i + 1


# função para executar o quicksor
def quicksort(array, low, high):
    if low < high:
        # encontra um elemento pivo tal que
        # os elementos menores que o pivot estejam a esquerda
        # os elementos maiores que o pivot estejam a direita

        pi = partition(array, low, high)

        # chamada recursiva a esquerda do pivot
        quicksort(array, low, pi - 1)

        # chamada recursiva a direita do pivot
        quicksort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print('unsorted array')
print(data)

size = len(data)
print('Sorted array in ascending order: ')
quicksort(data, 0, size - 1)
print(data)
