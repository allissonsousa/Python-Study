"""Crie um programa que tenha uma tuopla totalmete preenchida com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso"""
tulipa = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20 para ver sua escrita por extenso: '))
while True:
    if (num >= 0) and num <= 20:
        print(f'{num} escrito por extenso é {tulipa[num]}')
        break
    else:
        num = int(input('Digite um número de 0 a 20 para ver sua escrita por extenso: '))
