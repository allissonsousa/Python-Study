"""Usada pra modelar tempo decorrido entre eventos
tempo de espera, ou ate acontecer algum evento, por exemplo
Tem relação interessante com a poisson
Contagem de numero de ocorrencias, se quisermos a probabilidade do tempo ocorrido entre uma ocorrencia e outra
ou numero de ocorrencia com o uso de poisson"""


"""Exemplos 
Decaimento radioativo
Tempo associado de produção de uma peça defeituosa
Medir a probabilidade proxima da queda de ativos
Medir o tempo até q um novo cliente entre na loja"""

"""Por exemplo, uma loja quer calcular a probabilidade de um cliente fazer uma compra a apos 3 minutos no site
usar lambda == 1/2"""

from scipy.stats  import expon

#definir a media lambda
lambda_ = 1/2

#calcular a probabilidade com scipy
prob = expon.cdf(3, scale = 1/lambda_)

#exibir resultado
print(prob)