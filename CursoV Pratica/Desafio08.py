# Escreva um programa que leia um valor em metros e o exiba em contimetros e milimetros

met = int(input('Valor em metros:'))
cent = met * 100
mil = cent * 10

print(f'Se convertida para centimetros a medida será de : {cent} centimetros \nSe convertida para milímetros a '
      f'medida será de: {mil} milimetros')