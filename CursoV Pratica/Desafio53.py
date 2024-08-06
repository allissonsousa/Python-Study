"""Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsidere os acentos e espaços
Palindromo: palavras q sao o mesmo de tras pra frente e de frente pra traz, ex = subi no onibus"""
f = str(input('Digite aqui a sua frase: ')).split()
f2 = ''.join(f).upper()
fi = str(f2[::-1])      # aqui usei fatiamento no lugar do for
if fi == f2:
    print('Estra frase é sim um palindromo')
else:
    print(f2)
    print(fi)

# CORREÇÃO
frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
jun = ''.join(pal)
inver = ''
for letra in range(len(jun)-1, -1, -1):     # foi da ultima letra até a primeira, voltando -1
    inver += jun[letra]
print(inver, jun)
if inver == jun:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')