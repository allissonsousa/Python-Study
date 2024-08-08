""" Faça um programa que leia um número qualquer e mostre o seu fatorial
ex :
5! = 5 x 4 x 3 x 2 x 1 = 120
Faça com WHILE e também faça com o uso do FOR"""

n = int(input('Digite um número e descubra o seu fatorial:\n')) + 1
x = n-1
ac1 = 0
ac2 = 0
ac3 = 0
while n != 1:
    n -= 1
    x -= 1
    if n != x:
        ac1 = n * x
        ac2 = ac1 * (x-1)
    print(n, x, ac1, ac2, ac3)
