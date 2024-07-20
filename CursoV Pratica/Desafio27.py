"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e o ultimo nome
separadamente
EX >> Ana maria de Sousa
primeiro Ana
ultimo sousa"""
nome = str(input('Digite aqui seu nome completo:'))
pri = str(nome.split()[0])
ult = str((nome.split()[::-1])[0])
print(f'Seu primeiro nome: {pri}\n'
      f'Seu último nome: {ult}')

"""Uso do ::-1 para inverter a ordem das palavras da frase que ja foi separada pelo split"""
