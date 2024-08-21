# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considere US$1,00 = R$3,27

# COMO FIZ
saldo = float(input('\033[1;31;47mDigite o seu saldo: R$\033[m'))
# colocar o r$ pra garantir q o usuario nao vai escrever letras
dol = saldo / 3.27

print(f'Com este saldo você pode comprar US${dol:.2f} dolares')  # uso do  .2f pra limitar quantos nm tem depois da virg
