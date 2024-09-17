"""Crie um programa onde o usuário possa digitar cinco  valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção ( sem usar o metodo, sort(). No final, mostre a lista ordenada na tela"""
ls = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    ls.append(n)

for i in range(0, len(ls)):
    minindex = i
    for d in range(minindex, len(ls)):
        if ls[minindex] > ls[d]:
            (ls[minindex], ls[d]) = (ls[d], ls[minindex])
print('==' * 20)
print(f'Os valores digitados em ordem foram: {ls}')

# CORREÇÃO

lista = list()
for c in range(0,5):
    num = int(input('Digite um valor:'))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('O valor foi adicionado no fim da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print('-=-' * 30)
print(f'Os valores digitados foram {lista}')
