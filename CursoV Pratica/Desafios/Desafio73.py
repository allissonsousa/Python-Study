"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a = Apenas os 5 primeiros colocados
b = Os utlimos 4 colocados da tabela
c = uma lista com os times em ordem alfabetica
d = em que posição na tabela esta o time Avai"""
tulipa = ('Fluminense', 'Corinthians', 'Vasco da Gama', 'São Paulo', 'Grêmio', 'Internacional', 'Flamengo', 'Palmeiras',
          'Santos', 'Cruzeiro', 'Curitiba', 'AtleticoMG', 'AtleticoPR', 'Bota Fogo', 'Vitoria', 'Goias', 'Bahia',
          'AtleticoGO', 'Sport', 'Avai')
print(tulipa[0:5])
print(tulipa[16:])
print(sorted(tulipa))
print(tulipa.index('Avai') + 1)
