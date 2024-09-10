"""Procura numa lista [] a posição em que pode ser encaixado ou encontrado um elemento x
target = 5
lista = [1, 3, 4, 6]
output = 3"""


def InsertPosition(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        tuple(nums)
        nums.sort()
        return nums.index(target)


lista = [1, 2, 3, 7]
objetivo = 5
print(InsertPosition(lista, objetivo))