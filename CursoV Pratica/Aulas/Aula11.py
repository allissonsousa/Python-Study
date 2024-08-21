# COLORINDO TEXTO NO TERMINAL PY
# Uso de código ANSI, separa a estilização com ponto e virgula e finaliza com uma leta M
"""\033[ *estilo da fonte* ; *cor do texto* ; *cor de fundo* m"""
# ex :
"""\033[0;33;44m"""
# Codigos para estilo :
# 0 == Nenhum, padrão
# 1 == Negrito
# 4 == Sublinhado
# 7 == inverte as cores de fundo e de letra.

# Códigos para cor de texto sendo as 30.. e de fundo sendo as 40.. :
# 30 == branco == 40
# 31 == vermelho  == 41
# 32 == verde == 42
# 33 == amarelo == 43
# 34 == azul == 44
# 35 == magenta == 45
# 36 == ciano == 46
# 37 == cinza. == 47

# Para usar mais cor deve se usar outras bibliotecas

# Casos especiais:
# Letra cinza e fundo preta: \033[m
# Letra preta e fundo branco: \033[7;30m
# Na sintaxe o codigo vem antes do texto, mas entre as mesmas ''
a = 3
b = 5
print(f'Os valores são \033[33m{a}\033[m e \033[31m{b}\033[m !!!')
print('\033[7;33;44mOlá, mundo\033[m')  # pra parar a formatação vc escreve o codigo sem formatação no final do texto

# Usando  dicionario pra pré setar as cores
nome = 'Alin'
cores = {'Limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('Ola amarelo {}{}{}'.format(cores['azul'], nome, cores['Limpa']))  # Uso do .format