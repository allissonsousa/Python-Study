# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
# sobre ele

# Forma q eu fiz

coisa = input('Digite algo:')
print(type(coisa))
print('É um \033[31mnúmero\033[m? :', coisa.isnumeric(), 'É \033[32mpalavra\033[m ou \033[31mnúmero\033[m? :'
      , coisa.isalnum(), 'É \033[33mletra\033[m? :', coisa.isalpha(),
      'Esta escrito em \033[34mminúsculo\033[m? :', coisa.islower(), 'É \033[35mimprimivel\033[m? :'
      , coisa.isprintable(), 'É \033[36mdecimal\033[m ? :', coisa.isdecimal())

# Forma ideal e corrigida

a = input('Digite algo:')
print('O \033[31mtipo primitivo\033[m desse valor é:', type(a))
print('Só tem \033[31mespaços\033[m ?', a.isspace())
print('É um \033[32mnúmero\033[m ?', a.isnumeric())
print('É \033[33malfabetico\033[m ?', a.isalpha())
print('É \033[34malfanumérico\033[m ?', a.isalnum())
print('Está em \033[35mmaiúscula\033[m ?', a.isupper())
print('Esta \033[36mcapitalizado\033[m ?', a.istitle())
