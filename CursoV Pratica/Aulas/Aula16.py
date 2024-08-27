lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')   # tuplas ficam entre parenteses
# tuplas são imutáveis
print(len(lanche))
print(lanche)
"""for i in lanche:
    print(i)"""

"""for cont in range(0, len(lanche)):
    print(lanche[cont])"""

print(sorted(lanche))

nume = ('6', '5', '1', '7')
print(sorted(nume))

A = (2, 5, 4)
B = (5, 8, 1, 2)
C = A + B
print(C)
print(C.index(8))
del(C)  # deleta a tupla