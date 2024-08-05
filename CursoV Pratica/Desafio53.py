"""Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsidere os acentos e espaços
Palindromo: palavras q sao o mesmo de tras pra frente e de frente pra traz, ex = subi no onibus"""
f = str(input('Digite aqui a sua frase: ')).split()
f2 = ''.join(f).upper()
fi = str(f2[::-1])
if fi == f2:
    print('Estra frase é sim um palindromo')
else:
    print(f2)
    print(fi)


