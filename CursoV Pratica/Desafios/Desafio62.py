"""Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos, O programa encerra quando
ele disser que quer mostrar 0 TERMOS"""
pri = int(input('Digite aqui o primeiro termo da sua PA: '))
ra = int(input('Digite aqui a razão da sua PA: '))
per = 0
qua = 10
pa = pri + (qua * ra)
termo = pri
print('Estes são os primeiros 10 termos da sua PQ')
print(pri)
while termo != pa:
    termo += ra
    if termo == pa:
        per = int(input('Quantos termos a mais voce deseja mostrar? '))
        if per != 0:
            qua += per
            pa = pri + qua * ra     #tenho q começar a usar nomes semanticos pras variaveis urgente
        else:
            break
    print(termo)
print(f'Estes são so {qua} primeiros termos da sua PA!')

# CORREÇÃO
print('Gerador de PA')
print('-=-' * 20)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
termo = pri
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, ' >> ', end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('FIM')