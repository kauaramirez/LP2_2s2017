from lms import *

def test_matricular():
    assert  Matricula(1700251,'si')==  'aluno matriculado em si'
    assert  Matricula(1700251,'si')==  'aluno ja matriculado'
    assert  Matricula(1700742, 'redes') == 'aluno matriculado em redes'

def test_aplicar():
    assert AplicarTeste(1700251) == 'pode realizar o teste'
    
def test_Enviados():
    assert MostrarEnviados() == ListaAlunosQueFizeram

def test_Nao_Enviados():
    assert MostrarNaoEnviados() == ListaAlunosQueNaoFizeram

def test_Media():
    assert media(7,6,9,2) == 'aprovado'



