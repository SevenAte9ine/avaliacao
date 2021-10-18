from Furadeira import Furadeira
from Lixadeira import Lixadeira
while True:
  selecao = input ("""Por favor, selecione se deseja registrar uma Furadeira ou uma Lixadeira.
  Insira 1 para uma Furadeira, ou 2 para uma Lixadeira. 
  Insira aqui: """)
  if selecao == "1":
    f1 = Furadeira (None,None,None,None)
    f1.potencia = input ("Insira a potência desta Furadeira: ")
    f1.nome = input ("Insira o nome: ")
    f1.tensao = input ("Insira o valor de tensão: ")
    f1.preco = input ("Insira o preco: ")
    f1.getInformacoes ()
    f1.cadastrar ()
  if selecao == "2":
    l1 = Lixadeira (None,None,None,None)
    l1.rotacoes = input ("Insira quantas rotações esta lixadeira pode fazer por minuto: ")
    l1.nome = input ("Insira o nome: ")
    l1.tensao = input ("Insira o valor de tensão: ")
    l1.preco = input ("Insira o preco: ")
    l1.getInformacoes ()
    l1.cadastrar ()
