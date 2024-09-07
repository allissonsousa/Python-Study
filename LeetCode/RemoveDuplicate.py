""" Remover elementos duplicados de uma lista"""
"""Fazer o código com listas linkadas"""


def removeDuplicado(lis):
    nlis = []
    for i in lis:
        if i not in nlis:
            nlis.append(i)
    return nlis


lista = [1, 1, 2, 2, 3, 3, 3, 3]
print(removeDuplicado(lista))
