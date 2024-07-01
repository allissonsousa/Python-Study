# Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor

# COMO EU FIZ
num1 = int(input('Digite um número inteiro:'))
num0 = num1 - 1
num2 = num1 + 1
print(f'O número antecessor a este é {num0}, e o número sucessor a este é {num2} !')

#  MELHOR MANEIRA

num = int(input('Digite um número inteiro:'))
print(f'O número antecessor a este é {num - 1}, e o número sucessor a este é {num + 1} !')

# dessa forma eu economizo memória, mas caso eu precise terei q criar as variáveis do antecessor e sucessor
