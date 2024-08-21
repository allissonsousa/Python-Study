# ESTRUTURAS DE REPETIÇÃO

# LAÇOS
"""for i in range(1, 12):
    passo
pega
------------------------------
for i in range(0,3):
    passo
    pula
passo
pega
------------------------------
for i in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega
"""
# --------------------
for i in range(6, 0, -1):       # Esse -1 vai tirando de um em um, por isso fica ao contrario
    print(i)
print('FIM')
# ---------------------
n = int(input('Digite um número:'))
for i in range(0, n+1):  # +1 serve para finalizar a contagem no numero q vc passou
    print(i)
print('FIM')
# ---------------------
c = int(input('Começo: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for i in range(c, f+1, p):
    print(i)
print('Fim')
# ---------------------
s = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores é {s}')