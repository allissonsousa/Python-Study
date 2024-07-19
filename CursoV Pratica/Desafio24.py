"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO """
cidade = str(input('Digite o nome de uma cidade:'))
pri = (str('SANTO' in cidade.upper().split()[0]))
print(pri.replace('False', 'Esta cidade não começa com a palavra santo').replace('True', 'Esta cidade começa com santo'))

""" Confuso um pouco, tem um verificador IN na frase que gera um resultado boleano, a frase antes de ser verificada
é colocada em maiusculo com upper e dividida com split e tem seu primeiro elemento isolado com o [0]
O str muda as palavras trye e false q antes era boleano, agora para string, e o replace muda seu conteudo"""