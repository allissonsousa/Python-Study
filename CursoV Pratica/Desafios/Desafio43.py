"""Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com
a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: obesidade
- Acima de 40: obesidade morbida
"""
print('Vamos calcular o seu IMC (Indíce de Massa Corporal)!')
peso = float(input('Qual o seu peso atual em kilos ? '))
altura = float(input('Qual a sua altura em metros ? '))
imc = peso / (altura * altura)  # ou (altura ** 2)
est = ''
if imc < 18.5:
    est = 'Abaixo do peso'
elif (imc < 25) and imc > 18.5:
    est = 'Peso ideal'
elif (imc < 30) and imc > 25:
    est = 'Sobrepeso'
elif (imc < 40) and imc > 30:
    est = 'Obesidade'
elif imc > 40:
    est = 'Obesidade morbida'
print(f'De acordo com a tabela de classificação, seu imc de {imc:.1f}, é categorizado como {est} !!')

# CORREÇÃO
# Simplificação dos teste

if imc < 18.5:
    est = 'abaixo do peso'
elif 18.5 >= imc < 25:  # Python é foda, aceita até comparação com essa formatação
    est = 'Peso normal'
elif 25 <= imc < 30:
    est = 'Sobrepeso'
elif 30 <= imc < 40:
    est = 'Obesidade'
else:
    est = 'Obesidade morbida'
print(f'De acordo com a tabela de classificação, seu imc de {imc:.1f}, é categorizado como {est} !!')