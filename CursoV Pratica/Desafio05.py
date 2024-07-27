# Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor

# COMO EU FIZ
num1 = int(input('Digite um número inteiro:'))
num0 = num1 - 1
num2 = num1 + 1
print(f'O número \033[36mantecessor\033[m a este é \033[35m{num0}\033[m, e o número \033[34msucessor\033[m'
      f' a este é \033[35m{num2}\033[m !')

#  MELHOR MANEIRA

num = int(input('Digite um número inteiro:'))
print(f'O número \033[36mantecessor\033[m a este é \033[34m{num - 1}\033[m, e'
      f' o número \033[35msucessor\033[m a este é \033[34m{num + 1}\033[m !')

# dessa forma eu economizo memória, mas caso eu precise terei q criar as variáveis do antecessor e sucessor
