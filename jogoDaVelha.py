from minmax import MinMax
from No import No
import copy

class JogoDaVelha:

    def __init__(self):
        self.jogo = (['*', '*', '*'],['*', '*', '*'],['*', '*', '*'])
        simbolos = ['X','O']

        aux = int(input("Selecione 0 para \"X\" e 1 para \"O\" \n"))

        while(aux != 1 and aux != 0):
            aux = int(input("Selecione 0 para \"X\" e 1 para \"O\" \n"))

        self.simbJogador1 = simbolos[aux]
        self.simbJogador2 = simbolos[not(aux)]
        self.estadoAtual = No(True, self.jogo)
        self.minMax = MinMax()
        self.estadoAtual.imprimir()
    
    def acabou(self):
        return self.estadoAtual.ganhou()

    def menu(self):
        auxY =  int(input("Selecione a linha ao qual deseja jogar \n"))
        
        while(auxY < 0 and auxY > 2):
            auxY = int(input("Selecione a linha ao qual deseja jogar \n"))

        auxX =  int(input("Selecione a coluna ao qual deseja jogar \n"))
        
        while(auxX < 0 and auxX > 2):
            auxX = int(input("Selecione a coluna ao qual deseja jogar \n"))

        return auxY, auxX

    def proximaJogada(self):
       
        x,y = self.menu()

        while(self.estadoAtual.estado[x][y] != '*'):
            print("Posição invalida\n")
            x,y = self.menu()    
        self.estadoAtual.estado[x][y] = self.simbJogador1
        self.estadoAtual.imprimir()

        aux = self.estadoAtual.ganhou()

        if(aux):
            return
            
        self.estadoAtual = self.minMax.miniMaxDecision(copy.deepcopy(self.estadoAtual), self.simbJogador2)
        self.estadoAtual.imprimir()

jogo = JogoDaVelha()
aux = jogo.acabou()

while(aux == False):
    jogo.proximaJogada()
    aux = jogo.acabou()