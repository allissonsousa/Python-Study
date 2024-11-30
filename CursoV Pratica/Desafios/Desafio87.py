"""Aprimore o desafio anterior, mostrando no final:
a soma de todos os valores pares digitados
a soma dos valores da terceira coluna
o maior valor da segunda linha"""
soma = terceira = maior = 0
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(valor)
        if valor % 2 == 0:
            soma += matriz[l][c]

        if c == 2:
            terceira += valor

        if l == 1:
            if valor > maior:
                maior = valor


print('-=-' * 30)

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}', end='')
    print()

print('-=-' * 30)
print(f'A soma dos valores pares é {soma}\n'
      f'A soma dos valores da terceira coluna é {terceira}\n'
      f'O maior valor da segunda linha é {maior}')
