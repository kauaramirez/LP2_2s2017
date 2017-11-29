def media(p1,t1,p2,t2):
    mediab1 = (p1*0.7) + (t1*0.3) 
    mediab2 = (p2*0.7) + (t2*0.3)
    mediafinal = mediab1 + mediab2 / 2
    if mediafinal >= 7:
        return 'aprovado'
    else:
        return 'exame'
       
        

TodosAlunos = []
ListaAlunosQueFizeram = []
ListaAlunosQueNaoFizeram = TodosAlunos
Ads = []
Si = []
Redes = []


def Matricula(ra,curso):

    if curso == "si":
        if ra in Si:
            return 'aluno ja matriculado'
        else:      
            Si.append(ra)
            TodosAlunos.append(ra)
            return 'aluno matriculado em si'

    if curso == "ads":
        if ra in Ads:
            return 'aluno ja matriculado'
        else:          
            Ads.append(ra)
            TodosAlunos.append(ra)
            return 'aluno matriculado em ads'
  
    if curso == "redes":
        if ra in Ads:
            return 'aluno ja matriculado'
        else:          
            Redes.append(ra)
            TodosAlunos.append(ra)
            return 'aluno matriculado em redes'
        
    return 'curso inválido'


def AplicarTeste(ra):

    if ra in ListaAlunosQueFizeram:
        return "Aluno já Realizou o reste"
    else:
        ListaAlunosQueFizeram.append(ra)
        ListaAlunosQueNaoFizeram.remove(ra)
        return "Pode realizar o teste"


def MostrarEnviados():
    return ListaAlunosQueFizeram

def MostrarNaoEnviados():
    return ListaAlunosQueNaoFizeram



'''
inserindo= AplicarTeste(5)
print (inserindo)
inserindo= AplicarTeste(5)
print (inserindo)


verificandofeitos = MostrarEnviados()
verificandonaofeitos = MostrarNaoEnviados()
print(verificandofeitos)
print(verificandonaofeitos)'''
