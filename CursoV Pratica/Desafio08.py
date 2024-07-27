# Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros

# COMO FIZ
met = int(input('Valor em \033[32mmetros\033[m: '))
cent = met * 100
mil = cent * 10

print(f'Se convertida para \033[34mcentimetros\033[m a medida será de : {cent} centimetros \n'
      f'Se convertida para \033[35mmilímetrosz\033[m a medida será de: {mil} milimetros')

# OUTRA FORMA DE SER FEITO
medida = float(input('Distancia em metros:')) # Uso do float para valores não inteiros
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m em centimetros é {cm} e em milimetros é {mm}')

# AGORA COM KM HM DM M DM CM MM >>
med = float(input('Valor em metros:'))
km = med / 1000
hm = med / 100
dm = med / 10
dc = med * 10
ctm = med * 100
mml = med * 1000
print(f'Tabela de conversões de {med}m:\n'
      f'Kilometros = {km:}km\n'
      f'hectometros = {hm}hm\n'
      f'decametros = {dm}dm\n'
      f'metros = {med}m\n'
      f'decimetros = {dc}dc\n'
      f'centimetros = {ctm}cm\n'
      f'milimetros= {mml}mm')