"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar se o usuário quer ou não continuar
digitando valores"""
cont = 'SIM'
maior = 0
menor = 0
acumulador = 0
contador = 0
media = 0
while cont == 'SIM':
    n = int(input('Digite aqui um valor a ser armazenado: '))
    acumulador += n
    contador += 1
    cont = str(input('Você deseja continuar a digitar valores ? [Sim/Não]')).upper()
    media = acumulador / contador
    if n > maior:
        maior = n
    elif menor == 0:
        menor = n
        if n < menor:
            menor = n

print(f'''{'=-=' * 20}
Você digitou {contador} números;
A média desses números é {media:.2f};
O maior dentre esses valores é o número {maior};
O menor dentre esses valores é o número {menor}.''')
