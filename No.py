import copy

class No:

    def __init__(self, tipo, estado, pai):
        self.tipo = tipo
        self.estado = estado
        self.pai = pai

    def ehMax(self):
        return self.estado

    def imprimir(self):
        for linha in self.estado:
            for elemento in linha:
                print(elemento, end=" ")
            print()
        print() 

    def funcaoSucessora(self, simbolo):
        sucessores = []
        estado = self.estado

        for i,linha in enumerate(estado):
            for j,elemento in enumerate(linha):
                if elemento == '*':
                    aux = copy.deepcopy(estado)
                    aux[i][j] = simbolo
                    x  = No(not(estado),aux, self)
                    sucessores.append(x)
        return sucessores

    
    def testeTermino(self, no):
        for linha in no.estado:
            if('*' in  linha):
                return False
        
        return True


    def funcaoUtilidade(self):

        print()
        estado = self.estado

        for linha in estado:
            for elemento in linha:
                print(elemento, end=" ")
            print()

        for i in range(3):
            if(estado[i][0] == estado[i][1] and estado[i][1] == estado[i][2]):
                return 1
            if(estado[0][i] == estado[1][i] and estado [1][i] == estado[2][i]):
                return 1

        if(estado[0][0] == estado[1][1] and estado[1][1] == estado [2][2]):
            return 1

        if(estado[0][2] == estado[1][1] and estado[1][1] == estado[2][0]):
            return 1
        
        return 0