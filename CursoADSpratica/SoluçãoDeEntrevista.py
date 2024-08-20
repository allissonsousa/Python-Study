# Numeros de uma lista devem ser filtrados ate saber quais deles somam igual a um terceiro valor
# Ex:
# [1, 3, 6, 25, 34]   objetivo = 28    tem q descobrir quais 2 deles a soma é 28
# mostrar o resultado com a posição do elemento dentro da lista
lista = [10, 2, 6, 23, 17, 1, 8, 64, 13]
objetivo = 15
temp = 0
soma = 0
while soma != objetivo:
    for i in lista:
        if i < objetivo:
            temp = i
            for ob in lista:
                if (temp + ob) == objetivo:
                    soma = temp + ob
                    print(temp, ob, soma)