"""Faça um programa que jogue par ou impar com o computador. O jog será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo"""
from random import choice, randint
resultado = ''
pare = ''
impopar = ''
acumulador = 0
print('._._' * 10)
print('VAMOS JOGAR IMPAR OU PAR')
print('._._' * 10)
while resultado != 'PERDEU':
    arra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pc = choice(arra)
    valor = int(input('Digite um valor: '))
    pain = str(input('Par ou impar? [P/I] ')).strip().upper()
    soma = pc + valor
    if soma % 2 == 0:
        pare = 'P'
        impopar = 'PAR'
    else:
        pare = 'I'
        impopar = 'IMPAR'
    if pare == pain:
        resultado = 'VENCEU'
        acumulador += 1
    else:
        resultado = 'PERDEU'

    print('-' * 30)
    print(f'Voce jogou {valor} e o computador {pc}. Total de {soma} deu {impopar}')
    print('-' * 30)
    print(f'Voce {resultado}!')
    print('=-=' * 10)

print(f'GAME OVER ! Você venceu {acumulador} vezes.')

# CORREÇÃO
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}, total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print(f'Vamos jogar Novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
