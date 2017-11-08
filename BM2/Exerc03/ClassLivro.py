class Livro():

    def __init__(self,nomes,qtddepag,autores,precos):
        self.nomes = nomes
        self.qtddepag = qtddepag
        self.autores = autores
        self.precos = precos

    def gPreco(self):
        return self.precos

    def sPreco(self,altpreco):
        self.precos = altpreco
        return self.precos