# criar uma saudação ao usuário

nome = input('Qual o seu nome?')
print('É um prazer te conhecer ,', nome)


# formatação diferente

nome = input('Qual seu nome?')
print('É um prazer te conheçer, {} !' .format(nome))  # o {} é substituido pelo conteúdo do .format

# outra formatação

nome = input('Qual seu nome?')
print(f'É um prazer te conheçer, {nome}!')  # uso do print(f'{}')
