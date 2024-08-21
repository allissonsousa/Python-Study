# Numeros de uma lista devem ser filtrados ate saber quais deles somam igual a um terceiro valor
# Ex:
# [1, 3, 6, 25, 34]   objetivo = 28    tem q descobrir quais 2 deles a soma é 28
# mostrar o resultado com a posição do elemento dentro da lista
lista = [12, 1, 43, 23, 5, 76, 13, 78, 45, 100]
objetivo = 123
temp = ob = soma = pri = seg = 0
while soma != objetivo:
    for i in lista:
        if i < objetivo:
            temp = i
            for ob in lista:
                if (temp + ob) == objetivo:
                    soma = temp + ob
                    pri = temp
                    seg = ob
                    break

print(f'[{lista.index(temp)}, {lista.index(seg)}]')