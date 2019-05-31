import copy
from No import No

class MinMax:

    def maxValue(self, no, simbolo):
        if(no.testeTermino()):
            return no.funcaoUtilidade(self.aux[simbolo])

        v  = -9999999
        sucessores = no.funcaoSucessora(self.aux[simbolo])

        for filho in  sucessores:
            v = max(v, self.minValue(filho, not(simbolo)))

        no.setIndice(v)
        return v

    def minValue(self, no, simbolo):
        if(no.testeTermino()):
            return no.funcaoUtilidade(self.aux[simbolo])

        v  = 9999999
        sucessores = no.funcaoSucessora(self.aux[simbolo])

        for filho in sucessores:
            v = min(v, self.maxValue(filho, not(simbolo)))

        no.setIndice(v)
        return v


    def miniMaxDecision(self, no, simbolo):
  
        self.aux = ['X','O']

        v = self.maxValue(no, True)

        for filho in no.filhos:
            if v == filho.getIndice():
                return copy.deepcopy(filho)
