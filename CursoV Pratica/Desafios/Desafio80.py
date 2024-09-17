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


