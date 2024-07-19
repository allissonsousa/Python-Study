"""Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra A
-Em que posição ela aparece a primeira vez
- Em que posição ela aparece a ultima vez"""
frase = str(input('Digite aqui uma curta frase:'))
quant = str(frase.upper().count('A'))
loc1 = frase.find('a')
loc2 = frase.rfind('a')
print(f'A letra "A" apareceu {quant} vezes nesta frase!\n'
      f'A letra "A" apareceu pela primeira vez na posição {loc1} !\n'
      f'A letra "A" apareceu pela ultima vez na posição {loc2} !')
