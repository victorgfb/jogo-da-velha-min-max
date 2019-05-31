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
            v = max(v, self.minValue(filho,simbolo))

    def minValue(self, no, simbolo):
        if(no.testeDeTermino):
            return no.funcaoUtilidade()

        v  = 9999999

        for filho in  no.funcaoSucessora(simbolo):
            v = min(v, self.maxValue(filho,simbolo))

aux = MinMax()
#print(aux.testeDeTermino([['X','O','X'],['O','X','O'],['O','X','O']]))
