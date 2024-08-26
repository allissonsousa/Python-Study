"""Faça uma função que leia um número e retorne uma lista ordenada
numero = 90382
ordenada = 0 2 3 8 9"""


def ordenada(num):
    termo = 0
    alist = []
    menor = []
    for i in range(0, len(num)):
        alist.append(int(num[i]))
    print(alist)

    for i in range(-1, len(alist)):
        termo = alist[i]
        for c in range(0, len(alist)):
            if alist[c] > termo:
                termo = alist[c]
                menor.append(termo)
            print(menor)





numero = '34520'
print(ordenada(numero))