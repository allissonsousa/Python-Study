"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras minusculas
- O nome com todas as letras maiusculas
- Quantas letras aotodo ( sem considerar espaços)
- Quantas letras tem o primeiro nome"""
nome = input('Digite aqui o seu nome completo:')
letras = int(len(nome))
esp = nome.count(' ')
total = letras - esp
print(f'Nome com todas as letras maiúsculas: {nome.upper()}\n'
      f'Nome com todas as letras minusculas: {nome.lower()}\n'
      f'Quantidades de letras ao todo: {total}\n'
      f'Quantidades de letras do primeiro nome: {len(nome.split()[0])}')

# IMPORTANTE = Nunca esquecer de que a contagem deve começar em zero
