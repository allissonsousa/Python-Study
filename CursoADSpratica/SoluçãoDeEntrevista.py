# Numeros de uma lista devem ser filtrados ate saber quais deles somam igual a um terceiro valor
# Ex:
# [1, 3, 6, 25, 34]   objetivo = 28    tem q descobrir quais 2 deles a soma é 28
# mostrar o resultado com a posição do elemento dentro da lista
lista = [1, 4, 12, 23, 5, 2, 11, 6, 45, 3]
objetivo = 15
soma = 0
while soma < objetivo:
    for i in range(0, len(lista)):
        if i < objetivo:
            soma += i