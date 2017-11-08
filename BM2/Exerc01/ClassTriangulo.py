class Triangulo():

    def __init__(self,ldA,ldB,ldC):
        self.ldA = ldA
        self.ldB = ldB
        self.ldC = ldC

    def calculoperimetro(self):
        self.result = self.ldA + self.ldB + self.ldC
        return self.result

    def Ladomaior(self):
        self.ladomaior = max(self.ldA, self.ldB, self.ldC)
        return self.ladomaior