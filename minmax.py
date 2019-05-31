class MinMax:

    def __init__(self, simbolo = 'X'):
        self.simbolo = simbolo

    def funcaoUtiliade(self, estado):

        print()
        
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

aux = MinMax()
print(aux.funcaoUtiliade([['X','O','X'],['O','X','O'],['O','X','O']]))
