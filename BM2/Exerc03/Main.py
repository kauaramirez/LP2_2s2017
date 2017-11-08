from ClassLivro import *

def ex02(self,nomes,qtddepag,autores,precos,alt):
    livro = Livro(nomes,qtddepag,autores,precos)
    #print("O preço do livro é :" .format(livro.getPreco()))
    preco = livro.sPreco(alt)
    #print("O novo preço do livro é:" .format(livro.getPreco()))
    return preco