import copy
from No import No

class MinMax:

    def __init__(self, simbolo = 'X'):
        self.simbolo = simbolo
        self.raiz = No(True, (['*', '*', '*'],['*', '*', '*'],['*', '*', '*']), None)

        lista = self.raiz.funcaoSucessora(self.simbolo)
        for no in lista:
            no.imprimir()

    def maxValue(self, no, simbolo):
        if(no.testeDeTermino):
            return no.funcaoUtilidade()

        v  = -9999999

        for filho in  no.funcaoSucessora(simbolo):
            if(filho.testeDeTermino):
                if(count == None):
                    count = 0
                count +=  self.maxValue(filho,simbolo)
            else:
                v = max(v, self.minValue(filho,simbolo))
        
        if(count != None):
            v = count
        return v

    def minValue(self, no, simbolo):
        if(no.testeDeTermino):
            return no.funcaoUtilidade()

        v  = 9999999
        count = None

        for filho in  no.funcaoSucessora(simbolo):
            if(filho.testeDeTermino):
                if(count == None):
                    count = 0
                count +=  self.maxValue(filho,simbolo)
            else:
                v = min(v, self.maxValue(filho,simbolo))

        if(count != None):
            v = count
        return v

    def miniMaxDecision(self, no, simbolo):
        v = self.maxValue(no,simbolo)

aux = MinMax()
#print(aux.testeDeTermino([['X','O','X'],['O','X','O'],['O','X','O']]))
