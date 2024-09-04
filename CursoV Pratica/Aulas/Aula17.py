# LISTAS

valores = [8, 2, 5, 4, 9, 3,  9]
valores.sort()      # Ordena a lista em ordem crescente
valores.sort(reverse=True)  # Ordena a lista em ordem descrescente
len(valores)    # Quantos elementos tem na lista

# PRÁTICA
num = [2, 5, 9, 1, 6]
num[3] = 1
num.append(12)
num.sort(reverse=True)
num.pop(2)
num.insert(2, 0)
print(num)

vals = []
vals.append(2)
vals.append(5)
vals.append(7)

for v in vals:
    print(f'{v} ...')

for c, v in enumerate(vals):            # c é posição do elemento V
    print(f'Na posição {c} encontrei o valor {v}')

a = [2, 3, 4, 7]
b = a
b[2] = 8       # Essa alteração vai acontecer nas duas listas pois elas foram igualadas, e assim estão conectadas
c = a[:]        # Para não acontecer essa ligação, usa-se fatiamento dos elementos
c[2] = 5
print(f'Lista a {a}')
print(f'Lista b {b}')
print(f'Lista c {c}')