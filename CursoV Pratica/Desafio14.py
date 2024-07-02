# Conversão de temperatura em graus °C para graus °F

c = float(input('Informe a temperatura em °C:'))
f = ((9 * c) / 5) + 32  # formula matemática para a conversão, também funciona sem os parenteses devido a precedencia
'''9 * c / 5'''
input(f'A temperatura de {c}°C corresponde a {f}°F ! ')
