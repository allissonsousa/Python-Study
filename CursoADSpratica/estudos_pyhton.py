#exercicios e estudos do meu Curso de ADS

import datetime
import urllib.request

import matplotlib


#exercicio 1 objetivo é fazer a multiplicação de um fatorial

#estratégia 1

def fatorial_interativo(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

#estratégia 2
def fatorial_recursivo(n):
    if ((n==0)or(n==1)):
        return 1
    return n*fatorial_recursivo(n-1)

numero = input('Digite aqui um numero:')
print(f'O fatorial de {numero} é: {fatorial_interativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')

#exercicio 2 objetivo é testar se um numero é ou nao primo

def eh_primo(n):
    if(n<2):
        return False
    i=n//2
    while(i>1):
        if(n%i==0):
            return False
        i=i-1
    return True
def imprimir_resultado(numero, resultado):
    mensagem= f'O numero {numero} Não é primo'
    if(resultado):
        mensagem= f'O numero {numero} é primo'
    return mensagem

numero = eval(input('Digite aqui o seu numero'))
resultado=eh_primo(numero)
msg=imprimir_resutado(numero, resultado)
print(msg)

#exercicio 3 objetivo criar um taximetro que calcule o valor da corrida

def taximetro(distancia,multiplicador=1):
    largada=3
    km_rodado=2
    valor=(largada+distancia*km_rodado)*multiplicador
    return valor

pagamento=taximetro(3.5)
print(pagamento)

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

#explicaçao de um conteudo
def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada+distancia*km_rodado)*multiplicador
    return valor
dist = eval(input('Entre com a distancia a ser percorrida em Km:'))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')

#IMPRIME O N-ESIMO VALOR DA SEQUENCIA FIBONACCI UTILIZA FUNCAO RECURSIVA
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
num = eval(input('DIGITE UM VALOR'))
print(fibo(num))

#IMPRIME O N-ESIMO VALOR DA SEQUENCIA FIBONACCI POREM ESTE UTILIZA DOCSTRING
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(help(fibo))

#aprendendo sobre o uso de bibliotecas em python
#exercicio para calcular uma equação de segundo grau ax².2b.c

def entrada_dados():
    coeficiente = quantidade = eval(input('Digite o valor do coeficiente: '))
    return coeficiente
def calc_delta(a,b,c):
    delta=b*b-4*a*c
    return delta

import numpy as np
def calcular_raizes(a,b,c,delta):
    if(delta<0):
        resultado='a equaçao não possui raizes nos números reais'
    elif(delta==0):
        x=-b/(2*a)
        resultado=f'a equação possui apenas a raiz: {x}'
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta)) / (2 * a)
        resultado=f'a equação possui as raizes: {x1} e {x2}'
    return resultado
#f(x)=ax^2b+bx+c
a=entrada_dados()
b=entrada_dados()
c=entrada_dados()

detla=calc_delta(a,b,c)

resultado=calcular_raizes(a,b,c,delta)
print(resultado)


#exercicio visualização de dados de vendas de produtos em forma de gráfico de barras
#tem que pesquisar a biblioteca
#muito louco kkkk


import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A', 'B', 'C', 'D'])
y=np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#Exercicio pra gerar 1000 pontos seguindo distribuiçao Normal(grafico e coisas que nao aprendi no ensino medio)com
# media de 2 e desvio padrao de 2
#exibir em um histograma
#krl o codigo é muito pequeno, foda demais

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1) #random randomiza os dados randomicos
dados = np.random.normal(loc=20, scale=2, size=1000) #normal quer dizer que esta trabalhando com distribuição normal
plt.hist(dados, color='lightblue', ec='red') #nao funcionou por causa de um bug do pycharm

#envio de email com smtplib que ja é um recurso dos modulos padroes do python
#essa parte é responsavel somente pela importaçao dos recursos nescessarios

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#agora sera feita o corpo do email desde o destinatario ate a mensagem enviada

msg=MIMEMultipart()
texto='Este e-mail foi enviado automaticamente atravez da linguagem python'

#parametros
senha='senha123'
msg['From']='allisson@outlook.com'
msg['To']='michellecastro.carlos@hotmail.com'
msg['Subject']='E-mail Python Estácio'

#criação do corpo da mensagem
msg.attach(MIMEText(texto,'plain'))

#agora os passos nescessarios para o envio automatico
#criaçao do servidor
server=smtplib.SMTP('smtp.outlook.com:587')
server.starttls()

#login na conta para envio
server.login(msg['From'],senha)

#envio da mensagem
server.sendmail(msg['From',msg['To'],msg.as_string()])

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')

#primeiro voce tem que crirar um email do google admin pra voce conseguir permitir apps menos seguros


#exemplo do uso de funcoes do modulo time , funcoes time e ctime
import  time
x=time.time()
print(f'Local time:{time.ctime(x)}')


#uso do modulo tkinter pra criar uma GUI de interacao grafica
from tkinter import *   #importaçao dos elementos disponiveis em tinker
janelaPrincipal=Tk()
janelaPrincipal.mainloop()

from tkinter import *

janelaPrincipal=Tk()
texto=Label(master=janelaPrincipal,text='Minha Janela Exibida')
texto.place(x=50,y=100)
janelaPrincipal.mainloop()

#Criando uma janela GUI com imagem e mais elementos, usando o tkinter

from tkinter import*

def funcClicar(): #definição da função para imprimir na tela 'Botao pressionado' ao clicar no botao
    print('Botão pressionado')

janelaPrincipal=Tk()
texto=Label(master=janelaPrincipal, text= 'Minha janela exibida') # é feita a criação do objeto Label para conter a
                                                                    # imagem e seu posicionamento
texto.pack()  #método pack(), que coloca o elemento centralizado e
# posicionado o mais perto possível do topo, depois dos elementos posicionados anteriormente.

pic=PhotoImage(file='bomdia.gif')
logo=Label(master=janelaPrincipal, image=pic)
logo.pack

botao=Button(master=janelaPrincipal,text='Clique Aqui', command=funcClicar) #criação do botao com text e command,
#o texto e a função a ser exibidas                                          # respectivamente
botao.pack()

janelaPrincipal.mainloop()

#_______________________________________________________________________________________________________________
#Tratamento de exções exercicio acompanhado
#criação de um código que trata um número, caso o usuario digite uma letra esta sera processada pela execao

try:                                       #try . tentando seguir o fluxo normal
    x=int(input('Digite um número:'))
except ValueError:        #Se digitar uma letra, o try(tentativa) vai falhar e vai gerar uma except(exceção) ValueError
    print('Entre com um número válido.')



#exercicio acompanhado, criaçao de um laco para continuar insistindo que o usuario escreva um valor numerico valido

while True:                                             #uso do while true para a criaçao de um laço
    try:  # try . tentando seguir o fluxo normal
        x = int(input('Digite um número:'))
        break                                            #o break so ocorre caso o try seja bem sucedido, caso contrario
                                                        #  o excepttoma lugar, gerando um ciclo
    except ValueError:  # Se digitar uma letra, o try(tentativa) vai falhar e vai gerar uma except(exceção) ValueError
        print('Entre com um número válido.')


#criaçao de um codigo que trata a excecao da divisao por 0

def dividir(x,y):
    try:
        resultado=x/y
        print('A divisão é: ', resultado)
    except ZeroDivisionError:
        print('Divisão por zero.')

dividir(3,0)


#uso de varias excepts dentro do mesmo try, para o tratamento de varias excecoes de uma unica vez

try:
    num=eval(input('Entre com um numero:'))
    print(num)
except ValueError:
    print('Mensagem 1')
except IndexError:
    print('Mensagem 2')
except TypeError:
    print('Mensagem 3')
except:
    print('Mensagem 4')                      #util para a amostragem de uma mensagem especifica para cada tipo de erro


""" Forma de tratamento geral de excecoes

try :
    Bloco 1
except Exception1:
    Bloco tratador de Exception1
except Exception2:
    Bloco tratador de Exception2
    ....
else:
    Bloco 2 - executado caso nenhuma excecao seja levantada
finally:
    Bloco 3 - executado independente do que ocorrer
Instruçao fora do try/except"""

#___________________________________________________________________________________________________________

#uso de python orientado a objetos,POO, usaremos classes neste exemplo
class Pessoa:
    def __init__(self, nome, ender):   #init é o construtor, self é um parametro de auto referencia, ou seja por esse
        self.set_nome(nome)            #parametro posso acessar os atributos e metodos desa classe, nomes e endereco
        self.set_ender(ender)          # sao atributos normais
    def set_nome(self, nome):     #atribuicao de nome para um atributo da propria classe, no momento ele é um atributo
        self.nome=nome         # do metodo, mas queremos que ele seja um atributo da classemuito, burocratico essa merda
    def set_ender(self, ender):
        self.ender=ender
    def get_nome(self):   #get feitos para retornar os atributos da classe para que sejam manipulados posteriormente
        return self.nome
    def get_ender(self):
        return self.ender

    #isso foi a criaçao da classe, agora precisamos criar um objeto para instanciar esta classe

pessoa1 = Pessoa("maria","rua 1223")

    #imprimir cada objeto

print((f'Nome:{pessoa1.get_nome()}, Endereço:{pessoa1.get_ender()}'))    #por algum motivo essa porra nao ta funcionando

#uso de herança e superclasse. Neste caso criarei uma classe filha de pessoa

class Profissional (Pessoa):
    def __init__(self,nome,idade,profissao):
        super().__init__(nome,idade)
        self.profissao=profissao
    def imprimir(self):
        super().imprimir()
        print("\t e trabalha como", self.profissao)
p=Profissional('Ana',25,'Balconista')
p.imprimir()

#-----------------------------------------------------------------------------------------

#AGREGAÇÃO em classes                       POR ALGUM MOTIVO NAO FUNCIONOU, FAZER FUNCIONAR MAIS TARDE

#Classe Salário
class Salario:      #primeiro self apenas por obrigatoriedade do python
    def __int__(self, base, bonus):
        self.base= base                           #o base recebe o valor 10000
        self.bonus=bonus                           #e o bonus recebe o valor 700

    def salario_anual(self):
        return(self.base*12)+self.bonus       #  <-----------------------------------------------------------------
                                                                                                                    #
#Classe empregado                                                                                                   #
                                                                                                                    #
class Empregado:                                                                                                    #
    def __int__(self,nome,idade,salario):                                                                           #
        self.nome=nome                                                                                              #
        self.idade=idade                                                                                            #
        self.salario_agregado=salario  #agregação     uso da classe Salario e Empregado ao mesmo tempo              #
    def salario_total(self):                  #pega o salario agregado,atributo de Salario, multiplicando o         #
        return self.salario_agregado.salario_anual()                        #salario base por 12 mais o bonus

#input/output
salario=Salario(10000,700)
emp=Empregado('Musashi',46,salario)
print(emp.salario_total())


#aqui esta instancioando a classe Salario e passando os valores de paramentros/atributos para o construtor(init)
#nome,idade e salario(sendo salario um itens instanciado de Salario oque causa uma agregação de classes)
#vem da classe Empregado

#----------------------------------------------------------------------------------------------
#METODO DE CLASSE X METODO ESTATICO

from datetime import date
class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        #metodo de classe para criar um objeto Pessoa através do ano de nascimento
    @classmethod           #uso de @ para sintaxe
    def apartirAnoNascimento(cls,nome,ano):     #parametro cls, para criação de classe
         return cls(nome,date.today().year-ano)
        #metodo estatico: verificar se é maior de idade
    @staticmethod
    def ehMaiorIdade(idade):
        return idade>=18  #comportamentos gerais
pessoa1=Pessoa('maria',26)
pessoa2=Pessoa.apartirAnoNascimento('Ana',2006)
print(pessoa1.idade)
print(pessoa2.idade)
#imprimir o resultado
print(Pessoa.ehMaiorIdade(17))
aaa

#------------------------------------------------------------------------------------------------

#uso do init para iniciar uma classe
#Criação de  dados de uma conta bancaria ipotetica
class Conta:
    def __init__(self,numero,cpf,nomeTitular,saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo

    def depositar(self, valor):
        self.saldo += valor
    '''def __sacar__(self,valor):
        self.saldo-=valor'''

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f'numero:{self.numero}\nCPF: {self.cpf}\nsaldo:{self.saldo}\n') #\n usado pra quebra da linha na
    def transfereValor(self,contaDestino,valor):                                #hora de imprimir
        if self.saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Transferencia Realizada')

    '''from Conta import Conta
    conta1 = Conta(1, 123, 'Joao', 0)
    conta2 = Conta(3, 456, 'Maria', 0)          
    conta1.depositar(1000)                     
    conta1.transfereValor(conta2, 500)          
    print(conta1.saldo)
    print(conta2.saldo)
    
    O uso desse codigo resultaria na exibição dos valores 500 e 500
     Em resumo, 1.000 reais foram depositados na conta1, enquanto foi realizada uma transferência no 
     valor de 500 reais para a conta2. No final, o saldo ficou 500 para conta1 e 500 para conta2.'''


    def main():
        c1 = Conta(1, 1, 'Joao', 1000)  # Objeto sendo instanciado
        print(f'Nome do titular da conta {c1.nomeTitular}')
        print(f'Número da conta: {c1.numero}')
        print(f'CPF do titular da conta:{c1.cpf}')
        print(f'Sado da conta: {c1.saldo}')
    if __name__ == '__main__':
        main()
    from Conta import Conta
    conta=Conta(,123,'Joao',0)                  #método sacar com retorno
    conta2=Conta(3,345,;'Maria',0)


# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script


#-------------------------------


#Segue um exemplo de uma classe sem um método construtor:
class A():
    def f(self):
        print('foo')

def main():
    obj_A = A() #objeto sendo instanciado
    obj_A.f()


#-------------------------------

#AGREGAÇÃO
    #Para atender a novas necessidades do sistema de conta corrente do banco,
    # agora é necessário adicionar uma funcionalidade
    # para o gerenciamento de conta conjunta, ou seja, uma conta corrente pode ter um conjunto de clientes associados

class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf=cpf
        self.nome=nome
        self.endereco=endereco

class Conta:
    def __init__(self,clientes,numero,saldo):
        self.clientes=clientes
        self.numero=numero
        self.saldo=saldo
    def depositar(self,valor):
        self.saldo+=valor
    def sacar(self,valor):
        if self.saldo<valor:
            return False
        else:
            self.saldo -=valor
            return True
    def transfereValor(self,contaDestino,valor):
        if self.saldo<valor:
            return ('Não existe saldo suficiente')
        else:
            contaDestino.depositar(valor)
            self.saldo-=valor
            return ('Transferencia Realizada')
    def gerarsaldo(self):
        print(f'numero:{self.numero} \n saldo:{self.saldo}')

    #Um programa testecontas.py deve ser criado para ser usado na instanciação dos objetos das duas classes e gerar
    # as transações realizadas nas contas dos clientes.

from contas import Conta
from clientes import Cliente
cliente1 = Cliente(123,'Joao','Rua 1')
cliente2 = Cliente(456,'Maria','Rua 2')
conta 1=Conta([cliente1,cliente2],1,0) #linha 5
conta1.geralsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
                        #Na linha número 5, é instanciado um objeto conta1 com dois clientes agregados:
                        #cliente1 e cliente2. Esses dois objetos são passados como parâmetros.


#----------------------------------------------------------------------------------------------------------------
    #COMPOSIÇÃO

 #A classe Conta ainda não está completa de acordo com as necessidades do sistema de conta corrente do banco.
    # Isso ocorre porque o banco precisa gerar extratos contendo o histórico de todas as operações realizadas
    # para conta corrente.
    # Para isso, o sistema precisa ser atualizado para adicionar uma composição de cada conta com
    # o histórico de operações realizadas. O diagrama a seguir representa a composição entre as classes Conta e Extrato.
    # Essa composição representa que uma conta pode ser composta por vários extratos.
    #A classe Extrato tem as responsabilidades de armazenar todas as transações realizadas na conta e de conseguir
    # imprimir um extrato com a lista dessas transações.

class Extrato:
    def __init__(self):
        self.transacoes=[]

def extrato(self,numeroconta):
    print(f'Extrato: {numeroconta} \n')
    for p in self.transacoes:
        print(f'{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime(%d/%b/%y)}')

#A classe Conta possui todas as transações, como sacar, depositar e transferir_valor. Cada transação realizada deve
    # adicionar uma linha ao extrato da conta.A composição Conta->Extrato inclusive precisa ser inicializada no
    # construtor da classe Conta .No construtor de Extrato, foi adicionado um atributo transações, o qual foi
    # inicializado para receber um array de valores

import datetime
from Extrato import Extrato

class Conta:
    def  __init__(self,clientes,numero,saldo):
        self.clientes=clientes
        self.nmumero=numero
        self.saldo=saldo
        self.sata abertura=datetime.satetime.today()
        self.extrato=Extrato()                          #Adição da linha nº 10 – criação de um atributo extrato,
                                                        # fazendo referência a um objeto Extrato.

    def depositar(self,valor):
        self.saldo +=valor
        self.extrato.transacoes.append(['DEPOSITO',valor,'DATA',datetime.datetime.today()]) #14

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= Valor
            self.extrato.transacoes.append(['SAQUE',valor,'DATA',datetime.datetime.today()])  #21
            return True

    def transfereValor(self,contadestino,valor):
        if self.saldo<valor:
            return 'Nao existe saldo suficiente'
        else:
            contadestino.depositar(valor)
            self.saldo -=valor
            self.extrato.transacoes.append(['TRANFERENCIA',valor,'DATA',datetime.datetime.today()])  #30
            return 'Transferencia realizada'

    def gerarsaldo(self):
        print(f'{self.numero}\nsaldo:{self.saldo}')

        #Adição das linhas nºs 14, 21 e 30– adição de linhas ao array de transações do objeto Extrato por meio do
        # atributo extrato.


    #--------------------------------------------------------------------------------------------------------

                #   ENCAPSULAMENTO

       #importancia do encapsulamento para a integrigade do codigo

def sacar(self, valor):
    if self.saldo<valor:
        return False
    else:
        self.saldo -=valor
        self.exterato.transacoes.append(['SAQUE',valor,'DATA',datetime.datetime.today()])
        return True

#------------------------------------------------------------------------------

        #PROPERTY

@property
def saldo(self):
    return self.saldo
#Os métodos decorados com a property @setter forçam todas alterações de valor dos atributos privados a passar por
    # esses métodos.
    #@< nomedometodo >.setter

@saldo.setter
def saldo(self, saldo):
  if (self.saldo < 0):
    print('saldo inválido')
  else:
    self._saldo = saldo      #Os properties ajudam a garantir o encapsulamento no Python.

    #Como acessar os metodos acessados pelo property

class Conta:
    def __init__(self,numero):
        self.numero=numero
        self._saldo=0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        if saldo < 0 :
            print('Saldo Inválido')
        else:
            self._saldo=saldo

def main():
    conta=Conta(1)
    conta.saldo=1000  #usando o @saldo.setter
    print(f'saldo da conta = {conta.saldo}') #usando o @property

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------------------------

    #  ATRIBUTOS DE CLASSE
#Suposto aplicativo para contar circulos no paint . exemplo

'''class Circulo():
    def __init__(self,pontox,pontoy,raio):
        self.pontox=pontox
        self.pontoy=pontoy
        self.raio=raio
'''
#No entanto, conforme mencionamos, é necessário controlar a quantidade
    # de círculos criados.o codigo acima vira esse de abaixo

class Circulo():
    _total_circulos=0
    #indicamos para o interpretador que seja criada uma variável total_circulos que está localizada
    # antes do init, o interpretador “entende” que se trata de uma variável de classe, ou seja,
    # que terá um valor único para todos objetos da classe.

    def __init__(self,pontox,pontoy,raio):
        self.pontox=pontox
        self.pontoy=pontoy
        self.raio=raio
        self._total_circulos+=1             #. Deve-se colocar a variável com atributo privado com o underscore ‘_’.

from Circulo import Circulo
    circ1=Circulo(1,1,10)
    circ1.total_circulos
    circ2=Circulo(2,2,20)
    circ2=total_circulos
    Circulo.total_circulos

    #ja é suposto que esse codigo nao funcione ja que nao tem um app pra ele ler, apenas para entender o conceito

#------------------------------------------------------------------------------------------------

        #MÉTODOS DE CLASSE     outro codigo de exemplo, sem funcionalidade

class Circulo:
    _total_circulos=0

    def __init__(self,pontox,pontoy,raio):
        self.pontox=pontox
        self.pontoy=pontoy
        self.raio=raio
        type(self)._total_circulos +=1

    @classmethod
    def get total_circulos(cls):  # criado o parâmetro cls como referência para classe
        return cls._total_circulos  #retornado o valor do atributo de classe _total_circulos

#--------------------------------------------------------------------------------------------------------

    #MÉTODOS PUBLICOS E PRIVADOS

            #Os dois underscores antes do método indicam que ele é privado:

class Circulo:
    def __init__(self,numero, saldo ):
        self.clientes=clientes
        self.numero=numero
        self.saldo=saldo

    def _gerarsaldo(self):   #definido o método __gerarsaldo como privado.Acessado apenas internamente pela classe Conta
        print(f'Numero: {self.numero}\n saldo:{self.saldo}')


#-----------------------------------------------------------------------------------------------------------

            #MÉTODOS ESTÁTICOS

import math
class Math:

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)     #Math foi chamado sem que um objet da classe Math fosse instanciado

    '''math.sqrt(20) >>>> 4.47213595499958'''

#------------------------------------------------------------------------------------------------------

            #AGREGAÇÃO DE CLASSES E MÉTODOS ESTATICOS PT2
#codigo para contagem de pessoas, no caso é usado metodos estaticos e privados para contagem ser geral da classe e não
#individual de cada objeto

class Pessoa:
    _contador=0  #atributo estatico fora do init, por padrao privado(a classe quebra um pouco essa regra)
    def __init__(self,nome,idade):  #recebe nome idade do objeto
        self.nome=nome
        self.idade=idade                    #ATRIBUTO
        Pessoa._contador+=1
    def imprimir(self):
        print(self.nome,'tem',self.idade,'ano(s)')

    @property  #propriedade para facilitar o acesso ao elemento estatico,o @é usado para decoração
    def contador(self):                     #PROPRIEDADE
        return type(self)._contador   #type de self, se type de self é pessoa ou idade este ira chamar pessoa ou idade

p1=Pessoa('Carlos',19)
print(p1.contador)
print(Pessoa._contador)

                #DECORAÇÃO>>> metadaddos associados a classe que auxiliam os compiladores
                #na transformaçao do codigo intermediario

#Código para separar nome e sobrenome de alguém
class NomeCompleto:
    def __init__(self,nome, sobrenome):
        self.nome=nome
        self.sobrenome=sobrenome
    @classmethod   #Médoto da classe         #PADRÃO FACTORY: criação de objeto apartir de qualquer informação
    def fromString(cls,texto):      #cls:class
        nome,sobrenome=map(str,texto.split('')) #mapeamento do texto e splitando(separando) o texto em partes,sendo
        ojeto=cls(nome,sobrenome)               #cada uma nome e sobrenome
        return object #chamada do construtor NomeCompleto e retornando o valor como objeto
registro1=NomeCompleto.fromString('Luiz Braga')

#Código para separar nome e sobrenome de alguém, igual o anterior com adição do método estático
class NomeCompleto:
    def __init__(self,nome, sobrenome):
        self.nome=nome
        self.sobrenome=sobrenome
    @classmethod
    def fromString(cls,texto):
        nome,sobrenome=map(str,texto.split(''))
        objeto=cls(nome,sobrenome)
        return objeto
    @staticmethod           #MÉTODO ESTATICO
    def isValid(texto):
        nomes=texto.split('')   #validação de palavras
        return len(nomes) > 1   #validação se o texto realmente contem 2 objetos (nome e sobrenome) retorna um booleano

#---------------------------------------------------------------------------------------------------

        #HERANÇA E POLIMORFISMO, E TRATAMENTO DE EXCEÇÕES

class ClasseSomaMultiplica:
    def __init__(self,a,b): #parametros a e b
        self.a=a  #atributos da classe a e b
        self.b=b
    def somar(self):
        return self.a+self.b #soma de a e b
    def multiplicar(self):
        return self.a*self.b

class Derivada(ClasseSomaMultiplica): #criação de herança com o uso de ()
    def subtrair(self):
        return self.a-self.b
    def dividir(self):
        return self.a/self.b

d = Derivada(10,20)  #instancia o objeto e os parametros
print(f'A soma de 10 e 20 é igual a :{d.somar()}')  #chama da funçao somar
print(issubclass(Derivada,ClasseSomaMultiplica))  #teste se a classe é ou nao derivada de uma classe mãe, valor booleano

#--------------------------------------------------------------------------------------------------------------

            #SOBRECARGA

    #Um passo antes do polimorfismo

    def somar(x,y,z=0):   #tres parametros na função, se eu nao passar o terceiro parametro o valor deste recebe 0
        return x+y+z

    print(somar(20,30))  #chamada do somar com dois parametros
    print(somar(20,30,50))  #chamada do somar com os tres parametros x y e z

    #Muito util em banco de dados

#------------------------------------------------------------------------------------------------------------------

            #POLIMORFISMO

class Argentina():
    def capital(self):
        print('Buenos aires é a capital da Argentina')
    def lingua_oficial(self):
        print('O Espanhol é a lingua ofcial da Argentina')

class Brasil():
    def capital(self):
        print('Brasilia é a capital do Brasil')
    def lingua_oficial(self):
        print('O Português é a lingua oficial do Brasil')

obj_arg=Argentina()  #criação de objetos
obj_bra=Brasil()
for pais in (obj_arg,obj_bra): #pais é uma variavel local
    pais.capital()
    pais.lingua_oficial()  #aqui acontece a mágica, pais em um momento se comporta como objeto argentina e em outro
                            #momento se comporta como objeto brasil
                            #para isso funcionar, ambas as classes devem ter os mesmos métodos


                            #OUTRO EXEMPLO DE POLIMORFISMO

class Veiculo:
    def rodar(self):
        print('Reduz o consumo de combustivel')

class VeiculoEletrico(Veiculo): #herda da classe veiculo
    def rodar(self):
        super().rodar()   #esse super faz referencia ao construtor da classe mae, quando chamar o método rodar vai
        print('Esse veículo utiliza eletricidade')              # aparecer as duas mensagens

veiculo_eletrico=VeiculoEletrico()
veiculo_eletrico.rodar()

#--------------------------------------------------------------------------------------------------------------------

                    #EXEMPLO DE EXCEÇÃO

x=10
if x>5:
    raise Exception('x não pode ser maior que 5. O valor de x foi de : {}' .format(x))

#esse exception ira gerar um alerta no console com a mensagem descrita caso a condição do if aconteça

#---------------------------------------------------------------------------------------------------------

                #HERANÇA MULTIPLA

        #Classe filha herda de duas ou mais superclasses, somente um exemplo


class ContaRemuneradaPoupanca(Conta, Poupanca):  #herdando das superclasses Conta e Poupanca
    def __init__(self, taxaremuneracao,clientes,numero,saldo,taxaremuneracao):

#-------------------------------------------------------------------------------------------------------------

                #IMPLEMENTANDO O POLIMORFISMO

#Polimorfismo é o mecanismo que permite a um método com o mesmo nome ser executado
# de modo diferente a depender do objeto que está chamando o método

#Código para banco que contem contas de tipos diferentes e descontos diferentes


import datetime
class ContaPoupança:
    def __init__(self,taxanumeracao):
        self.taxanumeracao=taxanumeracao
        self.data_abertura=datetime.datetime.today()

    def remuneracao(self):
        self.saldo+=self.saldo*self.taxanumeracao

class ContaCliente:
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        self.numero=numero
        self.IOF=IOF
        self.IR=IR
        self.valorinvestido=valorinvestido
        self.taxarendimento=taxarendimento

    def CalculoRendimento(self):
        self.valorinvestido+=(self.valorinvestido*self.taxarendimento)
        self.valorinvestido=(self.valorinvestido-(self.taxarendimento*self.IOF*self.IR))

    def Extrato(self):  #1  foi definido um método Extrato, que é igual para as três classes, ou seja, as subclasses
        print (f'O saldo atual da conta {self.numero}é {self.valorinvestido:10.2f}') # herdarão o código completo
                                                                                    # desse método

from ContaCliente import ContaCliente
class ContaComum(ContaCliente)
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        super().__init__(numeroIOFIR,valorinvestido,taxarendimento)

    def CalculoRendimento(self): #2
        self.valorinvestido+=(self.valorinvestido*self.taxarendimento)

from ContaCliente import ContaCliente
class ContaRemunerada(ContaCliente):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        super().__init__(numeroIOFIR,valorinvestido,taxarendimento)

    def CalculoRendimento(self): #3
        self.valorinvestido+=(self.valorinvestido* self.taxarendimento)
        self.valorinvestido-=self.valorinvestido*self.IOF

class Banco():
    def __init__(self,codigo,nome):
        self.codigo=codigo
        self.nome=nome
        self.contas=[]

    def adicionaconta(self,contacliente):
        self.contas.append(contacliente)

    def calcularendimentomensal(self): #7
        for c in self.contas:
            c.CalculoRendimento()

    def imprimesaldocontas(self):
        for c in self.contas:  #aqui tava faltando no codigo da sava


banco1= Banco(999,'teste')
contacliente1=ContaCliente (1,0.01,0.1,1000,0.5)
contacomun1=ContaComum(2,0.01,0.1,2000,0.5)
contaremunerada1=ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicionaconta(contacliente1) #(4), o objeto é da própria classe Conta Cliente.
banco1.adicionaconta(contacomun1) #(5), o objeto contacomoum1 passado é uma ContaComum, que passa no teste “É-UM
banco1.adicionaconta(contaremunerada1) #(6), o objeto contarenumerada1 “É-UM” objeto ContaComum
banco1.calcularendimentomensal() #7
banco1.imprimesaldocontas() #8 Pelo polimorfismo, o interpretador verificará o teste “É-UM”, porém esse método não
# foi sobrescrito pelas subclasses da hierarquia ContaCliente

#(4), (5) e (6), o banco adiciona todas as contas da hierarquia em um único método devido ao teste “É-UM”
# das linguagens orientadas a objetos
#(7), acontece a “mágica” do polimorfismo,pois, em (4), (5) e (6), são adicionadas contas de diferentes tipos
# para o array conta da classe Banco


#------------------------------------------------------------------------------------------------------------

            #CLASSE ABSTRATA

#Seguindo o codigo anterior, supomos que preciso tornar uma Conta Cliente abstrata

'''from abc import ABC
class ContaCliente(ABC):'''

from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        self.numero=numero
        self.IOF=IOF
        self.IR=IR
        self.valorinvestido=valorinvestido
        self.taxarendimento=taxarendimento

    @abstractmethod
    def CalculoRendimento(self):
        pass


#Quando se tentar instanciar um objeto da classe, será obtido um erro indicando que essa classe não pode ser instanciada
#-----------------------------------------------------------------------------------------------------------------------

            #TRATAMENTO DE EXCEÇÕES
#codigo para forçar uma excecao, nao funciona
'''class ExecaoCustomizada(exception):  #definição da exceção customizada com metodo pass que nao executa nada relevante
    pass

    def throws(): (2)      # método que se for chamado criará exceção na memória de ExecaoCustomizada
        raise ExecaoCustomizada
        try:                
            throws()
        except ExecaoCustomizada as ex:
            print('Exceção Lançada')'''

#try...except, que indica para o interpretador que a área do código localizada entre o try e o except poderá lançar
# exceções que deverão ser tratadas nas linhas de código após o except

#OUTRO EXEMPLO DE TRATAMENTO DE EXCECAO
try:
    print (x)    #não foi atribuido valor a x
except:
    print('Variavel indefinida')

#Mais um exemplo

class ExcecaoCustomizada(Exception):
    pass
x = -12
if x <0:
    raise Exception('Valor negativo!!!')
x = 'oi'
if not type(x) is int:
    raise TypeError('Use apenas inteiros')

#se o x for -12 ou 'ola' por exemplo o tratamento de excecoes entra em acao e mostra as mensagens de erro dando
#continuidade no funcionamento do codigo

#---------------------------------------------------------------------------------------------------------------

            #EXERCICIOS

#Criação de uma classe 'veiculo' e seus atributos de instancia

class Veiculo:
    def __init__(self,nome,vmaxim,kmlitro):
        self.nome=nome
        self.vmaxim=vmaxim
        self.kmlitro=kmlitro

    def toStr(self):                #toStr = para string
        print(f'Nome do carro:{self.nome}')
        print(f'Velocidade máxima:{self.vmaxim}Km/H')
        print(f'Kilometros por Litro:{self.kmlitro}')

modelo_carro=Veiculo('Fusca',100,13)
modelo_carro.toStr()

#Criação de uma classe filha de veiculo

'''class Onibus(Veiculo):
    pass   #pass usado para preencher sintaticamente a lacuna apos o class

onibus_escolar=Onibus('SulMinas',130,8)
onibus_escolar.toStr()'''

#Modificação da classe onibus adicionando o numero de assentos do veiculo
class Veiculo:
    def __init__(self,nome,vmaxim,kmlitro):
        self.nome=nome
        self.vmaxim=vmaxim
        self.kmlitro=kmlitro

    def capacidade_assentos(self,capacidade):   #esse metodo é nescessario para adicionar o parametro 'Capacidade'
        print(f'O numero de assentos do {self.nome} é {capacidade}')
    def toStr(self):                #toStr = para string
        print(f'Nome do carro:{self.nome}')
        print(f'Velocidade máxima:{self.vmaxim}Km/H')
        print(f'Kilometros por Litro:{self.kmlitro}')
class Onibus(Veiculo):
    def capacidade_assentos(self,capacidade=70):
        return super().capacidade_assentos(capacidade=70)


onibus_escolar=Onibus('SulMinas',130,8)
onibus_escolar.toStr()
onibus_escolar.capacidade_assentos()

#tudo foi mantido igual a classe como antes, exceto pelo capacidade_assentos

#------------------------------------------------------------------------------------------------------------

            #FUNÇÕES PURAS

#script funcao1.py

valor=20

def multiplica(fator):
    global valor
    valor=valor*fator
    print('Resultado',valor)

def main():
    numero=int(input())
    multiplica(numero)
    multiplica(numero)

if __name__ == '__main__':
    main()
# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual à "__main__".
# Nesse caso, a condição do IF a seguir será TRUE,
# então o que está no corpo do IF será executado.
# No caso, é um chamado ao método main do script


#script funcao2.py

valor=20

def multiplicador(valor,fator):
    valor=valor*fator
    return valor

def main():
    numero=int(input())
    print('Resultado',multiplica(valor,numero))
    print('Resultado',multiplica(valor, numero))

if __name__ == 'main':
    main()

#DADOS IMUTAVEIS

#script funcao 3.py
#captando os valores do campo Input

valores=input()
#separando os valores pelo espaço em branco e transformando-os em uma lista de inteiros
valores=[int(i)for i in valores.split()]

def  altera_lista(lista):
    lista[2]=lista[2]+10
    return lista

def main():
    print('Nova lista',altera_lista(valores))
    print('Nova lista',altera_lista(valores))

if __name__ == '__main__':
    main()

#script funcao4.py

#captando os valores do campo Input
valores=input()
#separando os valores pelo espaço em branco e transformando-os em uma lista de inteiros
valores=[int(i)for i in valores.split()]

def altera_lista(lista):
    nova_lista=list(lista)
    nova_lista[2] = nova_lista[2]+10
    return lista

def main():
    print('Nova lista',altera_lista(valores))
    print('Nova lista', altera_lista(valores))

if __name__ == '__main__':
    main()

#--------------------------------------------------------------------------------------------------------------

        #FUNÇÕES DE ORDEM SUPERIOR

#script funcao5.py

def multiplicar_por(multiplicador):
    def multi(multiplicando):
        return multiplicando*multiplicador
    return multi #espera um parâmetro chamado multiplicando, que será multiplicado pelo multiplicador passado como
                 # parâmetro para a função “pai”
def main():
    multiplica_por_10=multiplicar_por(10)
    print(multiplica_por_10(1))
    print(multiplica_por_10(2))

    multiplica_por_5=multiplica_por(5)
    print(multiplica_por_5(1))
    print(multiplica_por_5(2))

if __name__=='__main__':
    main()

#ao ser chamada com um determinado multiplicador como argumento, retorna uma nova função multiplicadora por
# aquele multiplicador e que tem como parâmetro o número a ser multiplicado (multiplicando).

#ESTUDAR ISSO EM VIDEO AULA, MEIO COMPLICADO

#-----------------------------------------------------------------------------------------

        #FUNÇÕES LAMBDA

def multiplicar_por(multiplicador):
    return lambda multiplicando:multiplicando*multiplicador

def main():
    multiplicar_por_10=multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))

    multiplicar_por_5=multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))

if __name__ == '__main__':
    main()

#---------------------------------------------------------------------------------------

            #FUNÇÃO MAP

#Todas as funções abaixo têm o mesmo resultado porém são obtidos de maneira diferente

#funcao com iteraveis

lista=[1,2,3,4,5]

def triplica_itens(iterable):
    lista_aux=[]
    for item in iterable:
        lista_aux.append(item*3)
    return lista_aux

def main():
    nova_lista=triplica_itens(lista)
    print(nova_lista)

if __name__=='__main__':
    main()





#funcao map

lista=[1,2,3,4,5]
def triplica(item):
    return item*3

def main():
    nova_lista=map(triplica,lista)
    print(list(nova_lista))

if __name__=='__main__':
    main()

#A função map garante a imutabilidade dos iteráveis passados como argumento. Como a função map retorna um iterável
# utilizamos o construtor list (iterável) para imprimir o resultado (linha 9).

#Funcao lambda e map

lista=[1,2,3,4,5]]

nova_lista=map(lambda item:item*3,lista) #função lambda

def main():
    print(list(nova_lista))

if __name__=='__main__':
    main()


#---------------------------------------------------------------

            #FILTER

#Todos fazem a mesma filtragem. Recebem uma lista e retornam os elementos ímpares, gerando uma nova lista,
# de forma a garantir a imutabilidade.

lista =[1,2,3,4,5]
def impares(iterable):
    lista_aux=[]
    for item in iterable:
        if item %2!=0:
            lista_aux.append(item)
    return lista_aux

def main():
    nova_lista=impares(lista)
    print(nova_lista)

if __name__ == '__main__':
    main()




#usando filter dessa vez


lista = [1,2,3,4,5]
def impar(item):
    return item %2!=0

def main():
    nova_lista=filter(impar,lista)
    print(list(nova_lista))

if __name__ == '__main__':
    main()



#usando filter e lambda

lista = [1,2,3,4,5]
nova_lista=filter(lambda item: item %2!=0,lista)

def main():
    print(list(nova_lista))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------------


#uso de paradigma imperativo- imperativo pois da ordens, voce cordena passo a passo do codigo

numeros = [1,2,3,4]
total = 0
for numero in numeros:
    total += numero
print ('o total eh ', total)

#segundo exemplo

print('\nsegundo exemplo')
if True:
    print('Tudo certo')
else:
    print('ops')

#------------------------------------------------------------------------------------------


#uso de paradigma funcional- vc usa oque tem ao seu dispor, funcoes, classes etc para vc ordenar o codigo a fazer
#oque vc precisa, sem reescrever tudo

numeros = [1,2,3,4]
print('o total eh', sum(numeros))

#segundo exemplo
print('Tudo certo!'if True else 'ops')




#------------------------------------------------------------------------------------------------

        #MUTABILIDADE

#nao alterar variaveis e permanecer com a utilizaçao de funções puras a fim de correr o menor risco possivel de erros
#no codigo (efeito colateral) 

#_______________________________________________________________________________________

        #COMPUTAÇÃO CONCORRENTE EM PYTHON

        #Criação de threads e processos

from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)

def main():
    t = Thread(target=funcao_a,args=('Meu Thread',))
    t.start()
                                                            #método de criação do thread e do process são semelhantes
    m =Process(target=funcao_a,args=('Meu Processo',))
    m.start()


if __name__ == '__main__':
    main()

    #aqui nao ta funcionando pqpq  precisava de um numero recebido por um input, ex: 3
    #é assim que ta no conteudo do curso ent ta certo



#MULTIPLAS THREADS E PROCESSOS

#criação de 10 threads e/ ou processos, laço de 10 iterações que criamos e iniciamos cadea thread ou processo

#threads
from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []

def funcao_a(indice):
    for i in range (10000):
        minha_lista.append(1)
        print('Termino thread', indice)

def main():
    tarefas=[]
    for indice in range(10):
        tarefa=Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print('Antes de guardar o termino!',len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print('Após guardar o termino!',len(minha_lista))


if __name__ == '__main__':
    main()


#PROCESSOS

from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []

def funcao_a(indice):
    for i in range(10000):
        minha_lista.append(1) #append é usado pra adicionar um item em um final de uma lista já existente
        print('Termino thread', indice)


def main():
    tarefas = []
        for indice in range(10): #por algum motivo nao ta aceitado o for, ent é isso
            tarefa = Process(target=funcao_a, args=(indice,))
            tarefas.append(tarefa) #append é usado pra adicionar um item em um final de uma lista já existente
            tarefa.start()

    print('Antes de aguardar o termino!', len(minha_lista))

for tarefa in tarefas:
    tarefa.join()

    print('Após aguardar o termino!', len(minha_lista))

if __name__ == '__main__':
    main()


                #USO DE TRAVAS LOCK

from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0

def funcao_a(indice):
    global contador
    for i in range(100000):
        contador +=1
    print('Termino thread', indice)

def main():
    tarefas = []
    for indice in range(10):
        tarefa=Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)     #append é usado pra adicionar um item em um final de uma lista já existente
        tarefa.start()

    print('Antes de aguardar o termino!', contador)

    for tarefa in tarefas:
        tarefa.join()

    print('Após aguardar o termino!', contador)


if __name__ == '__main__':
    main()

##detalhe sobre o APPEND = (append), na visão do GIL, é atômico, ou seja, ele é executado de forma segura e não pode
# ser interrompido no meio de sua execução.

#outro exemplo de Lock


from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0
lock = Lock()  #uso do construtor lock()
print_lock=Lock()

def funcao_a(indice):
    global contador
    for i in range(100000):
        lock.acquire()
        contador +=1
        lock.release()
    print_lock.acquire()
    print('Termino thread', indice)
    print_lock.release()

def main():
    tarefas = []
    for indice in range(10):
        tarefa=Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print('Antes de aguardar o termino!', contador)

    for tarefa in tarefas:
        tarefa.join()

    print('Após aguardar o termino!', contador)

if __name__ == '__main__':
    main()


#DICA =  ARGS SERVE COMO UM ARRAY QUE RECEBE OS DADOS DA COMMAN LINE, NO MOMENTO DA EXECUÇÃO PODEMOS ENVIAR  UMA
#INFORMAÇÃO POR MEIO DELE

#________________________________________________________________________________________________________


        #COMPARTILHANDO VARIAVEIS ENTRE PROCESSOS

#riaremos uma variável do tipo inteiro e a compartilharemos entre os processos.
# Essa variável fará o papel de um contador e a função paralelizada vai incrementá-la:
#o código abaixo foi copiado direto do curso, provavelmente nao funcionao por nao compatibilidade ed IDE


from threading import Thread
from multiprocessing import Process, Value, Lock

def funcao_a(indice, cont):
    for i in range(100000):
        with cont.get_lock():    #construtor da classe value, VARAIVEL COMPARTILHADA
            cont.value +=1
    print('Termino processo', indice)

def main():
    contador=Value('i',0)
    lock= Lock()
    tarefas =[]
    for indice in range(10):
        tarefa=Process(target=funcao_a, args=(indice, contador, lock)) #Como não temos acesso a variáveis globais entre
                            # os processos, precisamos passar esta para o construtor process por meio do parâmetro args
        tarefas.append(tarefa)
        tarefa.start()

    print('Antes de aguardar o termino!', contador.value)

    for tarefa in tarefas:
        tarefa.join()

    print('Após aguardar o termino!', contador.value)

if __name__ == '__main__':
    main()

#Como a passagem de parâmetros é posicional, o parâmetro índice da funcao_a recebe o valor da variável índice e o
# parâmetro cont recebe uma referência para a variável contador (linha 15).


#MAIS EXERCÍCIOS DE CRIAÇÃO DE THREADS E PRPOCESSOS

#EXERCÍCIO 1: THREADS

import threading #importação da biblioteca nescessária pra criação de threads
import time         #o mesmo, porém pra contagem de tempo

#exemplo de função sem parâmetros

def funcao():
    for i in range(3):   #para o indice no range, criar uma lista de 3 itens
        print(i,'Executando thread!')   #exibição do indice, e da string, um por vez
        time.sleep(1)           #aguardo de tempo entre a execução do ciclo do programa, 1 s pra casa ciclo do range

print('Iniciando o programa!')
threading.Thread(target=funcao).start() #chamando o thread e chamando a função com o target e o start
time.sleep(3)   #usei esse sleep por causa do delay entre os ciclos do range
print('Finalizando programa!')




#EXERCÍCIO 2:

import threading
import time

#exemplpo de função com parametros
def funcao(mensagem):
    for i in range(3):
        print(i,'mensagem')
        time.sleep(1)

print('Iniciando o programa!')
x = threading.Thread(target=funcao,args=('Executando!',))
x.start()
time.sleep(3)
print('Finalizando o programa!')

#essa função tem o funcionamento bem semelhante a anterior




#EXERCÍCIO 3:

import threading
import time
#sincronizando threads
ls=[]  #variavel lista que recebera os valores após o programa terminar

def contador1(n):    #função contador com n como parametro
    for i in range(1,n+1):      #lista com parametro
        print(i)
        ls.append(i)    #item do range ira aprecer no ultimo espaço a direita da lista
        time.sleep(0.4)

def contador2(n):
    for i in range(6,n+1):
        print(i)
        ls.append(i)   #===
        time.sleep(0.5)

x=threading.Thread(target=contador1,args=(5,))
x.start()

y=threading.Thread(target=contador2,args=(10,))
y.start()

time.sleep(2.8)     #tive q adicionar esse delay por causa dos mesmos que tem nas funções, pra tudo ficar em ordem
print(ls)



#EXERCÍCIO 4:

#mesmo conceito de uso de threads e listas, porém desta vez usando urls no lugar de números
#no caso eu nao consegui instalar a biblioteca urlib2 entao esse codigo nao funciona nessa IDE


import threading
import urllib2
import time

start = time.time()
urls = ['https://www.google.com/?&bih=665&biw=1325&client=opera-gx&hs=Icu&hl=pt-BR',
        'https://estudante.estacio.br/disciplinas/estacio_7510384/temas/5/conteudos/1',
        'https://photos.google.com/explore']

def chama_url(url):
    req=urllib2.Request(url)
    response=urlib2.urlopen(req)
    the_page=response.read()
    print('$s\'carregando em $sS'%(url,time.time)- start)

threads = [threading.Thread(target=chama_url,args=(url,))for url in urls]
for thread un threads:
    thread.start()
for thread in threads:
    thread.join()

print('Elapsed time : %s'%(time.time()-start)


#EXERCICIO 5  - EXECUÇÃO DE UMA THREAD COM SLEEP DE 2S E INFORMANDO O INICIO E O FIM DA EXECUÇÃO DA THREAD

from time import sleep
from threading import Thread
def tarefa(tempo_espera, mensagem):
    print(f'\Iniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa{mensagem}')
thread=Thread(target=tarefa, args=(2,'Thread em execução')) #instanciamente de uma thread com nome thread
thread.start()                                              #inicio da execução da thread
print('\Aguardando pela execução da Thread ...')
thread.join()
print('A execução foi concluida')

#código funciona perfeitamente



#EXERCICIO 6  -  EXECUÇÃO DE DUAS THREADS, 1º E 2º THREAD ESPERAM 3 E 2 SEGUNDOS, INFORME DE EXECUÇÃO DAS THREADS

from time import sleep
from threading import Thread
def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciando tarefa{nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')

t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))
t1.start()
t2.start()
t1.join()  #esperar até completar a execução da thread 1
t2.join()   #esperar até completar a execução da thread 2
print('A execução foi concluida!')



#EXERCICIO 7 - EXECUÇÃO DE DUAS THREADS, 1º CALCULA O CUBO DE UM NUMERO, 2º CALCULA O QUADRADO DE UM NUMERO, DELAY DE
#3S E 2S, INFORME DA EXECUÇÃO DAS THREADS

from time import sleep
from threading import Thread
def calcular_cubo(num, tempo_espera):
    print(f'\nCubo:{num*num*num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_cubo')

def calcular_quadrado(num, tempo_espera):
    print(f'\nQuadrado: {num*num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_quadrado')

t1=Thread(target=calcular_quadrado, args=(5,3))
t2=Thread(target=calcular_cubo, args=(5,2))
t1.start()
t2.start()
t1.join() #esperar até completar a execução da thread 1
t2.join() #esperar até completar a execução da thread 2
print('A execução ja foi concluida!')

#_______________________________________________________________________________________________________________________

                        #MÓDULO 3

#DESENVOLVIMENTO WEB COM PYTHON

#O principal framework Python full-stack é o Django.
# Os principais frameworks não full-stack são o Flask e o CherryPy.

#Primeiro passos com o flask

from flask import Flask #importação do flask

app = Flask(__name__)   #criação de uma instância na classe flask, onde __nome__ é o argumento para q o flask localize
                        #elementos css e js nos arquivos

@app.route('/')  #criação de uma rota para a  url raiz da nossa aplicação, (/) decorador como parâmetro a rota, ou url
def ola_mundo():
    return 'Olá. mundo!'

if __name__ == '__main__':
    app.run()

#--------------------------------------------------------------------------------------------------------------------

                #ROTAS E PARÂMETROS

#APRIMORANDO ROTAS

#Exercicio bem parecido com o anterior, porém dessa vez funcional

from flask import Flask

app = Flask(__name__)

@app.route('/ola')  #o parâmetro do decorador @app.route da linha 5 agora é ‘/ola’
def ola_mundo():
    return 'Olá, mundo !'

if __name__ == '__main__':
    app.run


#criar, também, uma rota para a URL raiz da aplicação (@app.route(‘/’)).


from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Página principal'

@app.route('/ola')
def ola_mundo():
    return 'Olá mundo'

if __name__=='__main__':
    app.run()

  #ESSES CÓDIGOS IRÃO GERAR UMA URL DO SITE CRIADO

#--------------------------------------------------------------------------------------------------------------

#RECEBENDO PARÂMETROS

#O decorador de rota (route) permite q passe parametros para as funções, colocando o nome do parametro da função entre
#<e> na URL da rota

#Mudando a rota da função ola_mundo de forma que seja possivel capturar e retornar o nome passado como parâmetro

from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Página principal'

@app.route('/ola/<nome>')
def ola_mundo(nome):
    return 'Olá, '+ nome  #uso do recurso <e>

if __name__ == '__main__':
    app.run()

    #ao usarmos o <e> com o mesmo nome do parametro da funcao ola mundo, podemos adicionar qualquer valor após o fim da
    #URL e esse valor sera exibido após o  'OLA'


#POREM se tentarmos acessar a pagina somento com o /ola, ira dar erro
#pra isso temos q criar mais uma rota

from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Página princial'

@app.route('/ola/')              #esse ola é só pra nao ter erro
@app.route('/ola/<nome>')        #esse tem o mesmo papel do anterior
def ola_mundo(nome='mundo'):  #esse é pika, tem a função de adicionar mundo após o ola, note q a variavel nome ja teve o
                                #valor dado como mundo
    return 'Olá, ' + nome

if __name__ == '__main__':
    app.run()

#---------------------------------------------------------------------------------------------------------------


        #MÉTODOS HTTP E MODELOS


#MODELOS HTTP
#Usamos o parâmetro methods do decorador @app.route(), que espera uma lista de strings com o nome dos metodos aceitos
#No Web dev a varias formas de acessar uma url, no flask a mais usada é o GET, para explicitar outros metodos é
#nescessário explicitar na rota quais métodos serão aceitos


#Criação da rota para a função logar, como argumento uma lista de duas strings, Get e Post, ou seja, essa rota deve
#responder as requisições do tipo get e post

from flask import Flask, request #objeto request, temos acesso a muitas outras propriedades da requisição, como:
                                    # cookie, parâmetros, dados de formulário, mimetype etc.
app=Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return 'Página principal'

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome):
    return 'Ola,' + nome

@app.route('/logar', methods=['GET','POST'] #verificar o método que foi utilizado na requisição usamos o atributo method
def logar():
    if request.method == 'POST':
        return 'Recebeu get! Fazer login!'
    else:
        return 'Recebeu get! Exibir FORM de login.'

if __name__== '__main__':
    app.run()

#-----------------------------------------------------------------------------------------------------------------


#PYTHON EM DESENVOLVIMENTO WEB


        #UTILIZANDO MODELOS

#As funções no Flask precisam retornar algo. O retorno das funções pode ser uma string simples e até uma string
# contendo uma página inteira em HTML.Porém criar paginas assim é muito complicado, e implica no scape q é evita
#problemas de segurança
#por meio da extensão Jinja2, permite utilizar modelos (templates) que são arquivos texto com alguns recursos a mais,
# inclusive escape automático.

#ESSA PARTE SERÁ FEITA EM UM ARQUIVO SEPARADO NA PASTA TEMPLATES --!!


#EXERCICIO 1 - exibir 'pagina inicial' no endereco raiz da pagina, exibir mensagem 'ola mundo', no endereço ola da
#pagina e exibir a mensagem 'ola usuario' no endereço '/ola/nome_do _usuario' da pagina

from flask import Flask

app=Flask(__name__)   #aplicação, o name é a aplicação em execução

@app.route('/')   #quando o usuario digitar somente a raiz do site
def index():
    return 'Página principal'
@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):  #nome é uma palavra default, quando o usuario digitar /ola/ ira aparecer mundo
    return 'ola,' + nome + '!'  #uso de concatenação com  o sinal de mais +

if __name__=='__main__':
    app.run()    #o objeto de aplicaçao ira dar run




#EXERCICIO 2 - (ESSE EU VOU FAZER SOZINHO PRIMEIRO E DEPOIS COM A INSTRUÇÃO DO PROFESSOR )
#Exibir a mensagem ola programadores no endereço raiz,exibir ola usuario no endereço /user/ e exiba a mensagem Altere o
#endereço do browser e recarregue a pagina
#E exibir a mensagem Ola, nome_usuario , no endereço /user/nome do usuário

from flask import Flask

app=Flask(__name__)

@app.route('/')
def mensagem():
    return 'Olá, programadores'
@app.route('/ola/')
@app.route('/ola/user/')
def mensagem2():
    return 'Olá, usuário' \
           'Altere o endereço do browser e recarregue a pagina'
@app.route('/ola/user/<nome>')
def mensagem3(nome='usuario'):
    return 'Ola, ' + nome + '!'

if __name__ == '__main__':
    app.run()

#Esse foi o meu código que funciona, de uma forma meio mediocre mas funciona
#Agora ao modo que o professor escreveu.PQP O CARA METEU UM HTML DO NADA, NEM TINHA ISSO NAS EXIGENCIAS DO EXERCICIO AA
#Se eu soubesse dessa safadeza ia ter ficado tudo bem melhor

#SOLUÇÃO ::

from flask import Flask
app=Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!<h1>'
    link= '<p><a href= user/Usuário>Clique Aqui!</a></p>'
    return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome='Usuário'):
    personalizar= f'<h1>Olá, {nome} ! </h1>'
    instrucao='<p>Altere o nome do <em> endereço do browser</em> e recarregue a página.</p>'
    return personalizar+instrucao

if __name__ == '__main__':
    app.run(debug=True)

    #ESSA É A SOLUÇÃO DO PROFESSOR, mas tem um porem esse arquivo so funciona com o suporte de outro arquivo HTML
    #Entao seria nescessario criar um diretorio em uma pasta com os aquivos python e html
    #O código que faria esse arquivo funcionar seria o seguinte:::::

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('indice.html')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!<h1>'
    link = '<p><a href= user/Usuário>Clique Aqui!</a></p>'
    return boas_vindas + link


@app.route('/user/')
@app.route('/user/<nome>')
def user(nome='Usuário'):
    personalizar = f'<h1>Olá, {nome} ! </h1>'
    instrucao = '<p>Altere o nome do <em> endereço do browser</em> e recarregue a página.</p>'
    return personalizar + instrucao


if __name__ == '__main__':
    app.run(debug=True)



#EXERCICIO 3 - Exibir a mensagem 'ola porgramadores'no endereço raiz, com a mensagem no site 'entre com dois numeros'
#exibir a mensagem  '00' no endereço /somar
#Exibir a mensagem  '30'no endereço /somar/10/20

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas='<h1>Olá, programadores!</h1>'
    instr='<p>Entre com dois números</p> '
    return boas_vindas+instr

@app.route('/somar')
@app.route('/somar/<num01>/<num02>')
def soma(num01=0,num02=0):
    resultado=float(num01)+float(num02)
    return str(resultado)

if __name__=='__main__':
    app.run(debug=True)


#--------------------------------------------------------------------------------------------------------------


                    #MÓDULO 4 - CIÊNCIAS DE DADOS EM PYTHON

#As técnicas de KDD (FAYYAD, 1996), também conhecidas como mineração de dados, normalmente se referem à extração de
# informações implícitas, porém úteis, de uma base de dados.
#Esta tecnica é separada em 3 partes :  Pré processamento, mineração de dados, e pós processamento (uma imagem em
#documentos pode ilustrar o processo detalhado do kkd)

#O processo detalhado é, na seguinte ordem :

#1Coleta e integração = dados provenientes de diversas fontes sejam consolidados em uma única base de dados

#2Codificação =  transformar a natureza dos valores de um atributo , transformação de dados numéricos em categóricos —
# codificação numérico-categórica –, ou o inverso — codificação categórico-numérica.

#3Construção de atributos =  criar colunas em uma tabela, por exemplo, refletindo alguma transformação dos dados
# existentes em outras colunas, após a coleta e integração dos dados.

#4Limpeza de dados = complementação de dados ausentes, detecção de ruídos e eliminação de dados inconsistentes.

#5A partição dos dados = separação dos dados em dois conjuntos disjuntos. Um para abstração do modelo e conhecimento e
# outra para testes, avalição do modelo gerado
