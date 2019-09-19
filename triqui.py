TABLERO = [["", "|", "", "|", ""],
           ["------------------"],
           []]

TABLERO_2 = [
["", "", ""], ["", "", ""],["", "", ""]
]

JUGADORES = {'jugador1': True, 'jugador2': False}

class Triqui():

    jugar = True

    def __init__(self):
        pass

    def iniciarJuego(self):

        while(self.jugar):
            print(TABLERO_2)

            if JUGADORES['jugador1']:
                self.jugador1()
                JUGADORES['jugador1'] = False
                JUGADORES['jugador2'] = True
            elif JUGADORES['jugador2']:
                self.jugador2()
                JUGADORES['jugador1'] = True
                JUGADORES['jugador2'] = False


    def jugador1(self):
        print "Jugador 1: Inserte la coordenada donde desea poner X"
        i = input("Fila: ")
        j = input("Columna: ")

        while not (self.comprobarMatriz(i,j)):
            print "Posicion ocupada..."
            print "Jugador 1: Inserte la coordenada donde desea poner X"
            i = input("Fila: ")
            j = input("Columna: ")

        TABLERO_2[i][j]="X"

        if (self.comprobarTriqui()):
            print "Triqui del jugador "+self.comprobarTriqui()[1]
            self.jugar = False
        else:
            pass

    def jugador2(self):
        print "Jugador 2: Inserte la coordenada donde desea poner O"
        i = input("Fila: ")
        j = input("Columna: ")

        while not (self.comprobarMatriz(i,j)):
            print "Posicion ocupada..."
            print "Jugador 2: Inserte la coordenada donde desea poner O"
            i = input("Fila: ")
            j = input("Columna: ")

        TABLERO_2[i][j]="O"

        if (self.comprobarTriqui()):
            print "Triqui del jugador "+self.comprobarTriqui()[1]
            self.jugar = False
        else:
            pass

    def comprobarMatriz(self,x,y):
        if (TABLERO_2[x][y] is ""):
            return True
        else:
            return False

    def comprobarTriqui(self):
        #Primera coordenada en X, segunda coordenada en Y
        #Diagonal I-D
        if (TABLERO_2[0][0]=="X" and TABLERO_2[1][1]=="X" and TABLERO_2[2][2]=="X") or (TABLERO_2[0][0]=="O" and TABLERO_2[1][1]=="O" and TABLERO_2[2][2]=="O"):
            return [True, TABLERO_2[0][0]]
        #Diagonal D-I
        elif (TABLERO_2[0][2]=="X" and TABLERO_2[1][1]=="X" and TABLERO_2[2][0]=="X") or (TABLERO_2[0][2]=="O" and TABLERO_2[1][1]=="O" and TABLERO_2[2][0]=="O"):
            return [True, TABLERO_2[0][2]]
        #Columnas
        elif (TABLERO_2[0][0]=="X" and TABLERO_2[0][1]=="X" and TABLERO_2[0][2]=="X") or (TABLERO_2[0][0]=="O" and TABLERO_2[0][1]=="O" and TABLERO_2[0][2]=="O"):
            return [True, TABLERO_2[0][0]]
        elif (TABLERO_2[1][0]=="X" and TABLERO_2[1][1]=="X" and TABLERO_2[1][2]=="X") or (TABLERO_2[1][0]=="O" and TABLERO_2[1][1]=="O" and TABLERO_2[1][2]=="O"):
            return [True, TABLERO_2[1][0]]
        elif (TABLERO_2[2][0]=="X" and TABLERO_2[2][1]=="X" and TABLERO_2[2][2]=="X") or (TABLERO_2[2][0]=="O" and TABLERO_2[2][1]=="O" and TABLERO_2[2][2]=="O"):
            return [True, TABLERO_2[2][0]]
        #Filas
        elif (TABLERO_2[0][0]=="X" and TABLERO_2[1][0]=="X" and TABLERO_2[2][0]=="X") or (TABLERO_2[0][0]=="O" and TABLERO_2[1][0]=="O" and TABLERO_2[2][0]=="O"):
            return [True, TABLERO_2[0][0]]
        elif (TABLERO_2[0][1]=="X" and TABLERO_2[1][1]=="X" and TABLERO_2[2][1]=="X") or (TABLERO_2[0][1]=="O" and TABLERO_2[1][1]=="O" and TABLERO_2[2][1]=="O"):
            return [True, TABLERO_2[0][1]]
        elif (TABLERO_2[0][2]=="X" and TABLERO_2[1][2]=="X" and TABLERO_2[2][2]=="X") or (TABLERO_2[0][1]=="O" and TABLERO_2[1][1]=="O" and TABLERO_2[2][1]=="O"):
            return [True, TABLERO_2[0][2]]
        else:
            return False



