# DICIONÁRIOS OU VÁRIAVEIS COMPOSTAS

dados = {'nome':'Pedro', 'idade':'25'}
'''A identação dos elementos do dicionario pode ser nomeada
Exemplo, ao invez de colocar dados[0] que seria pedro no caso de uma lista, coloca-se dados['nome'] por exemplo'''
print(dados['nome'])
'''Para criar um novo elemento no dicionário vc usa o comando:
dados['sexo'] = 'M' que cria-ra uma nova unidade de armazenamento chamada sexo, que contem o dado M'''
dados['sexo'] = 'M'
'''Para apgar elementos, se usa o metodo del:
del dados['idade'] '''
del dados['idade']
filme = {
    'titulo' : 'Star wars',
    'ano' : 1977,
    'diretor' : 'George Lucas'
}
#Cada elemento ou identação do dicionário se chama chave ou key
#Para obter os valores: print(filme.values())
#Para obter as identações: print(filme.keys())
#Para obter ambos: print(filme.items())

#Pode ser usado um equivalente do enumerate em dicionários:
for k, v in filme.items():
    print(f'O {k} é {v}')

#Pode tambem combinar listas e dicionários colocando um dentro do outro:

locadora = [{'Titulo': 'Star wars', 'Ano': 1977, 'Diretor': 'George Lucas'},
            {'Titulo': 'Avengers', 'Ano': 2012, 'Diretor': 'Josh Whedon'},
            {'Titulo': 'Matrix', 'Ano': 1999, 'Diretor': 'Machowski'}]

#Agora além da identação da lista, tambem tem as chaves do dicionario:
print(locadora[0]['Ano'])

pessoas  = {'Nome':'gustavo', 'sexo':'m', 'idade':45}

brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'sao paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

#--------------------------------
#problemas com fatiamento e copia de dados em dicionário
estado = dict()
pais = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['Sigla'] = str(input('Siga do estado:'))
    brasil.append(estado.copy())   #se fosse lista, usariamos [:] fatiamento, porém dicionarios nao sao fatiaveis
    # por isso é usado o metodo copy
print(brasil)
for e in brasil:
    for v in e.values():
        print(v)