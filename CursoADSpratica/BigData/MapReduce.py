"""O objetivo desse codigo é receber um tento com diversas palavras e contar quantas vezes cada uma apareceu"""
from mrjob.job import MRJob
import re       #trata expressões regulares

palavra_regex =  re.compile(r"[\w']+")     #recebe uma linha de texto e retorna uma lista() com as palavras

class QuantidadeDePalavras(MRJob):  #classe que herda caracteristicas do pacote mrjob (mapear e reduzir)
    def mapper(self, _ ,linha):
        for p in palavra_regex.findall(linha):
            yield p.lower(), 1

    """No metodo mapper, processamos cada linha e geramos pares de palavras que sao as keys e do valor 1 no reducer,
    obtendo a quantidade de vezes que a palavra apareceu"""

    def reducer(self, p, qtd):
        yield p, sum(qtd)

    """Inicia o ciclo de vida do código"""

if __name__ == '__main__':
    QuantidadeDePalavras.run()

"""Para executar o código deve-se colocar o endereço do arquivo txt e o comando de inicialização do código"""
""" python texto_exemplo.txt > qtd.txt 
O programa ira gerar um arquivo qtd.txt que mostrará a contagem das palavras"""
