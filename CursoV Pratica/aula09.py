# CADEIA DE TEXTO
# Fatiamento
frase = 'Eu sou muito legal sabia?'  # Essa string tem 12 caracteres enumerados de 0 a 11
print(frase)  # Resulta no print total da frase
print(frase[9])  # Resulta no print do nono caractere = i
print(frase[9:13])
# Resulta no print dos caracteres do nono ao decimo terceiro, excludente o decimo terceiro ou seja = i-t-o
print(frase[9:21:2])
# Resulta no print do nono ao vigesimo caractere, porem com um gap de um em um digitos ex = babacao >> b_b_c_o
print(frase[:5])  # Omissão do primeiro caractere, logo começa desde o primeiro digito da string
print(frase[15:])  # Omissão do ultimo caractere, logo começa no 15° e vai ate o ultimo digito da string
print(frase[9::3])  # Começa no nove até o final, porem pulando de 3 em 3 caracteres >>> i g b
# Análise da string
print(len(frase))  # Mostra a quantidade de caracteres de frase/ len >> length
print(frase.count('o'))  # Conta quantas vezes a letra _O_ aparece na frase
print(frase.count('o', 0, 13))  # Faz a contagem da letra _o_ do caractere 0 até o caractere 12
print(frase.find('leg'))  # Mostra em qual indice começa essa parte da string
print(frase.find('Android'))  # String inexistente no find, retorna o valor -1 pq nao existe
print('sou' in frase)  # Retorna um valor boleano se existe ou nao essa palavra na string
# Transformação
print(frase.replace('legal', 'Burro'))  # Substitui a palavra existente por outra, legal por burro neste caso
print(frase.upper())  # Deixa todos os caracteres da frase em maiusculo
print(frase.lower())  # Deixa todos os  caracteres da frase em minusculo
print(frase.capitalize())  # Coloca a primeira letra da string em maiusculo e transforma o resto em minusculo
print(frase.title())  # Vai transformar o começo de todas as palavras pra maiusculo e o resto em minusculo
print(frase.strip())  # Remove todos os epaços desnecessarios do começo e do fim da frase se houver >> '  eu sou     '
print(frase.rstrip())  # Remove somente os espacos da direita ou seja do fim da frase
print(frase.lstrip())  # Remove somente os espaçoos da esquerda ou seja do começo da frase
# Divisão
print(frase.split())  # Divisao da string entre os espaços das palavras, cada palavra é indexada começando por 0
# Isso gera uma lista com cada palavra e cada palavra tendo seus caracteres começando por 0 >> 01234  01 012 01234
# Cada palavra recebe uma indexação começando por 0 >> 0 1 2 3
# Junção
print('-'.join(frase))  # Vai juntar todos as palavras da frase, caso tenha sido separado pelo split, e vai colocar um -
# Entre cada palavra

# Ultilidades
print(''' f ''')    # O print com aspas triplas faz a quebra automatica de linhas para um texto muito grande
print('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining 
essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum''')

print(frase.upper().count('O'))  # Primeiro a frase foi transformada em maiusculo, depois foi buscado o 'O'
print(len(frase.strip()))  # Caso a frase tenha espaços desnecessarios, faz a contagem sem consideralos
dividido = frase.split()
print(dividido[0])
# A frase foi dividida em palavras cada um recebendo uma indexação, o 0 seria a primeira palavra, exibe esta
print(dividido[2][3])
# Seleciona a palavra de indexaçao 2 e desta mesma pega a letra de indexação 3
