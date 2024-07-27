# criar uma saudação ao usuário

nome = input('Qual o seu nome?')
print('\033[32mÉ um prazer te conhecer\033[m,', nome)


# formatação diferente

nome = input('Qual seu nome?')
print('\033[33mÉ um prazer te conheçer\033[m, {} !' .format(nome))  # o {} é substituido pelo conteúdo do .format

# outra formatação

nome = input('Qual seu nome?')
print(f'\033[31mÉ um prazer te conheçer\033[m, {nome} !')  # uso do print(f'{}')
