from Ferramenta import Ferramenta

class Furadeira(Ferramenta):
  def __init__(self,potencia, nome, tensao, preco):
    self._potencia = potencia
    self.nome = nome
    self.tensao = tensao
    self.preco = preco

  @property
  def potencia(self):
    return self._potencia

  @potencia.setter
  def potencia(self,valor):
    self._potencia = valor

  def getInformacoes(self):
    print("Potência da furadeira: ", self._potencia)
    super().getInformacoes()

  def cadastrar(self):
    print("Furadeira cadastrada com sucesso.")