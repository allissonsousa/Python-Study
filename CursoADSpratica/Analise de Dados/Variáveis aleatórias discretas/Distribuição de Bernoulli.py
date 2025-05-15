from scipy.stats import bernoulli

# Definindo a probabilidade de sucesso como 0.7
p = 0.7

# Criando a distribuição de bernoulli
distribuicao = bernoulli(p)

# Calculando a PMF para o vaor 1 (sucesso)
probabilidade_sucesso = distribuicao.pmf(1)

# Exibindo a probabilidade de sucesso