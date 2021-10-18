from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):
  def __init__(self, rotacoes, nome, tensao, preco):
    self.__rotacoes = rotacoes
    self.nome = nome
    self.tensao = tensao
    self.preco = preco

  @property
  def rotacoes(self):
    return self.__rotacoes

  @rotacoes.setter
  def rotacoes(self, valor):
    admin = True
    if admin:
      self.__rotacoes = valor
    else:
      print("Açao não permitida")

  def getInformacoes(self):
    print("Rotações por minuto: ", self.__rotacoes)
    super().getInformacoes()

  def cadastrar(self):
    print("Furadeira cadastrada com sucesso.")