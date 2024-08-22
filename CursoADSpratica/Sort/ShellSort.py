# implementação de shell sort

def shellsort(arr):
    # começa com um espaço grande, e vai reduzindo
    n = len(arr)
    gap = n / 2

    # faz uma insersão com o gap do tamanho de gap
    # os primeiros elementos ja estao em gap
    # ordena estes adicionando mais um elemento ate q todo o array esta dentro de gap
    while gap > 0:
        for i in range(gap, n):
            # adiciona i aos elementos que foram ordenados em gap
            # salva i em temp e cria um espaço na posição de i
            temp = arr[i]

            # trocas os elementos recem trocados em gap ate que fiquem corretos
            # localiza i
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            # coloca temp (original i) na posição correta
            arr[j] = temp
        gap /= 2


arr = [12, 34, 54, 2, 3, 5]
n = len(arr)
print('Array antes da organizção')
for i in range(n):
    print(arr[i])

shellsort(arr)

print('Array depois da organização')
for i in range(n):
    print(arr[i])

