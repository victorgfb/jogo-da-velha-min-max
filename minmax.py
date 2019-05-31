import copy
from No import No

class MinMax:

    def maxValue(self, no, simbolo):
        if(no.testeTermino()):
            return no.funcaoUtilidade(simbolo)

        v  = -9999999
        sucessores = no.funcaoSucessora(simbolo)
        for filho in  sucessores:
            v = max(v, self.minValue(filho,simbolo))
        
        no.setIndice(v)
        return v

    def minValue(self, no, simbolo):
        if(no.testeTermino()):
            return no.funcaoUtilidade(simbolo)

        v  = 9999999
        sucessores = no.funcaoSucessora(simbolo)

        for filho in sucessores:
            v = min(v, self.maxValue(filho,simbolo))

        no.setIndice(v)
        return v

    def miniMaxDecision(self, no, simbolo):
        v = self.maxValue(no, simbolo)
        print(len(no.filhos))

        for filho in no.filhos:
            print(filho.getIndice())

        for filho in no.filhos:
            if v == filho.getIndice():
                return copy.deepcopy(filho)
