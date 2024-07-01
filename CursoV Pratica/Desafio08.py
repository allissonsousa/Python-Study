# Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros

# COMO FIZ
met = int(input('Valor em metros:'))
cent = met * 100
mil = cent * 10

print(f'Se convertida para centimetros a medida será de : {cent} centimetros \nSe convertida para milímetros a '
      f'medida será de: {mil} milimetros')

# OUTRA FORMA DE SER FEITO
medida = float(input('Distancia em metros:')) # Uso do float para valores não inteiros
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m em centimetros é {cm} e em milimetros é {mm}')

# AGORA COM KM HM DM M DM CM MM >>
