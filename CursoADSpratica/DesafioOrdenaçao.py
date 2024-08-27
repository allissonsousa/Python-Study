"""Faça uma função que leia um número e retorne uma lista ordenada
numero = 90382
ordenada = 0 2 3 8 9"""


def ordenada(num):
    alist = []
    size = len(num)
    for i in range(0, size):
        alist.append(int(num[i]))
    for i in range(0, size):
        minimo = i
        for c in range(0, size):
            if alist[i] >= alist[c]:
                minimo = c
            (alist[i], alist[minimo]) = (alist[minimo], alist[i])
    return alist


numero = '567281023'
print(ordenada(numero))

# OUTRA FORMA MAIS SIMPLES DE SER FEITO::
def ordem(n):
    list = []
    for i in range(0, len(n)):
        list.append(n[i])
    return sorted(list)


num = str(input('numero'))
print(ordem(num))
