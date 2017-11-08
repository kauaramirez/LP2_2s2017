class Alunos():

    def __init__(self,nomes,cursos,tempSdormir):
        self.nomes = nomes
        self.cursos = cursos
        self.tempoSdormir = tempoSdormir

    def Estudar(self,estudar):
        self.tempoSdormir = estudar-(self.tempoSdormir)
        return self.tempoSdormir

    def Dormir(self,dormir):
        self.tempoSdormir = dormir+(self.tempoSdormir)
        return self.tempoSdormir