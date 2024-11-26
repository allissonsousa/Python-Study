# LISTAS PART-2

# LISTAS DENTRO DE LISTAS
"""
PESSOA = [JOAO, 31]
PESSOAS.APPEND(PESSOA)>>
PESSOAS = [ [JOAO, 31], [MARIA, 23], [PEDRO, 13] ]

PRINT(PESSOAS[0][0]) == JOAO
PRINT(PESSOAS[1][1]) == 19

COPIA DE DADOS = [:]
"""

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
'''galera.append(teste)''' #aqui ha uma ligação entre as estruturas, ent maria22 ira repetir
galera.append(teste[:])     #por isso deve ser feito a COPIA do dado
print(galera)

#---------------------
# estrutura composta
galera = [['joao', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 35]]
print(galera[2] [1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
#--------------------
guys = list()
date = list()
for c in range(0, 3):
    date.append(str(input('Nome: ')))
    date.append(int(input('Idade: ')))
    guys.append(date[:])
    date.clear()

print(guys)
totmai = totmen = 0
for p in guys:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade')