import copy

class No:

    def __init__(self, tipo, estado):
        self.tipo = tipo
        self.estado = estado
        self.filhos = []

    def ehMax(self):
        return self.estado

    def imprimir(self):
        print()
        for linha in self.estado:
            for elemento in linha:
                print(elemento, end=" ")
            print()
        print() 

    def setIndice(self, indice):
        self.indice = indice

    def getIndice(self):
        return self.indice

    def ganhou(self):
        estado = self.estado

        for i in range(3):
            if(estado[i][0] == estado[i][1] and estado[i][1] == estado[i][2]):
                if(estado[i][0] != '*'):
                    return estado[i][0]
            if(estado[0][i] == estado[1][i] and estado [1][i] == estado[2][i]):
                if(estado[0][i] != '*'):
                    return estado[0][i]

        if(estado[0][0] == estado[1][1] and estado[1][1] == estado [2][2]):
            if(estado[0][0] != '*'):
                return estado[0][0] 

        if(estado[0][2] == estado[1][1] and estado[1][1] == estado[2][0]):
            if(estado[0][2] != '*'):
                return estado[0][2]
        
        return False

    def funcaoSucessora(self, simbolo):
        estado = self.estado
        self.filhos = []

        for i,linha in enumerate(estado):
            for j,elemento in enumerate(linha):
                if elemento == '*':
                    aux = copy.deepcopy(estado)
                    aux[i][j] = simbolo
                    x  = No(not(estado),aux)
                    self.filhos.append(x)
        return self.filhos

    
    def testeTermino(self):
        for linha in self.estado:
            if('*' in  linha):
                return False
        
        return True


    def funcaoUtilidade(self, simbolo):
        aux = self.ganhou()

        if(aux == simbolo):
            return 1
        elif(aux == False):
            return 0
        else:
            return -1