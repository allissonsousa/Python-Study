"""Controle estatistico de qualidade
Usada pra eventos raros
Usada em numeros de sinistros
"""
"""utilizada para investigar “eventos raros”. Se você quiser, por exemplo, estudar a probabilidade de infartos por
 dia em determinada cidade, usará a distribuição de Poisson, porque a incidência é muito pequena em relação ao total 
 de pessoas."""

"""Sintaxe:   stats.poissom.pmf(x,y)
Em média 3 clientes solicitam um remeio x por hora, qual a probabilidade de exatamente 2 clientes
solicitarem esse remédio em uma hora especifica
x= 2  probabiliade de caso especifico
y = 3  media de dados"""

from scipy.stats import poisson

prob = poisson.pmf(2,3)
print("Probabilidade de 2 clilentes solicitarem em uma hora: ", prob)

"""#probabilidade de k events ocorrerem com taxa meia y
probabilidade = poisson.pmf(k, lambda_)

#funcao de massa de probabillidade acumulada
probabiliade_acumulada = ppoisson.cddf(k, lambda_)

#gerar uma amostra aleatória da distribuição de poisson
amostra = poisson.rvs(lambda_, size)"""