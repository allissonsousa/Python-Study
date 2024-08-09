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
            pa = pri + qua * ra
        else:
            break
    print(termo)
print(f'Estes são so {qua} primeiros termos da sua PA!')