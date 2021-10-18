from abc import ABCMeta, abstractmethod, abstractproperty

class Ferramenta(metaclass=ABCMeta):

  nome = None
  tensao = None
  preco = None

  def getInformacoes(self):
	  print("Nome: " , self.nome )
	  print("Tensão: " , self.tensao )
	  print("Preço: " , self.preco )

  @abstractmethod
  def cadastrar(self):
    pass
