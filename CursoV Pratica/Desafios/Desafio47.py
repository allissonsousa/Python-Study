"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50"""
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print('FIM')

# CORREÇÃO
for i in range(2, 51, 2):   # Redução de quantas vezes o for faz o laço, reduz pela metade de vezes q ele percorre
    print(i)    # Pode tirar o if, pois o próprio range já está testando os pares
print('FIM')
# Economiza memória de processamento