""" Crire um programa que leia duas notas de  um aluno e calcule sua media, mostrando uma mensagem no final,
de acordo com a media atingida:
- media abaixo de 5?
REPROVADO
- Media entre 5 e 6,9:
RECUPERAÇÃO
- Media 7 ou superior:
APROVADA"""
print('Vamos descobrir a sua média!!')
n1 = float(input('Digite aqui a sua primeira nota: '))
n2 = float(input('Digite aqui a sua segunda nota: '))
media = float((n1 + n2) / 2)
if media < 5:
    print(f'Sua nota médio foi abaixo de 5 pontos, {media}. REPROVADO!!')
elif (media <= 6.9) and (media >= 5):
    print(f'Sua nota media não foi suficiente, {media}. RECUPERAÇÃO!!')
elif media >= 7:
    print(f'Sua nota média foi muito boa, {media}. APROVADO!!')