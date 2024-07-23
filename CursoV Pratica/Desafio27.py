"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e o ultimo nome
separadamente
EX >> Ana maria de Sousa
primeiro Ana
ultimo sousa"""
import ntpath

nome = str(input('Digite aqui seu nome completo:'))
pri = str(nome.split()[0])
ult = str((nome.split()[::-1])[0])
print(f'Seu primeiro nome: {pri}\n'
      f'Seu último nome: {ult}')

"""Uso do ::-1 para inverter a ordem das palavras da frase que ja foi separada pelo split"""

# CORREÇÃO
n = str(input('Digite seu nome completo: ')).strip()
name = n.split()
print(f'Muito prazer em te conheçer \n'
      f'Seu primeiro nome é : {name[0]}\n'
      f'Seu último nome é : {name[len(name)-1]}')
