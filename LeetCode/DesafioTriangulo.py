"""printe um triangulo retangulo na tela feito de varios asteriscos *
o tamanho (altura e base) do triangulo deve ser imputado na tela"""
base = int(input('Qual o tamanho da base do seu triangulo ?'))
acumulador = 0
while base > acumulador:
    acumulador += 1
    print(' * ' * acumulador)
