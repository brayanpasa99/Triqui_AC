TABLERO = [["", "|", "", "|", ""],
           ["------------------"],
           []]

TABLERO_2 = [
["", "", ""], ["", "", ""],["", "", ""]
]

class Triqui():

    def __init__(self):
        pass

    def iniciarJuego(self):

        jugar = True

        while(jugar):
            jugadores = {'jugador1': True, 'jugador2': False}

            print(jugadores['jugador1'], jugadores['jugador2'])

            if jugadores['jugador1']:
                self.jugador1();
                jugadores['jugador1'] = False;
                jugadores['jugador2'] = True;
            elif jugadores['jugador2']:
                self.jugador2();
                jugadores['jugador1'] = True;
                jugadores['jugador2'] = False;


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

        if (self.comprobarTriqui(1)):
            print "Triqui del jugador 1"
            jugar = False
        else:
            pass

    def jugador2(self):
        print "Jugador 2: Inserte la coordenada donde desea poner O"
        i = input("Fila: ")
        j = input("Columna: ")

        while (self.comprobarMatriz(i,j)):
            print "Posicion ocupada..."
            print "Jugador 2: Inserte la coordenada donde desea poner O"
            i = input("Fila: ")
            j = input("Columna: ")

        TABLERO_2[i][j]="O"

        if (self.comprobarTriqui(2)):
            print "Triqui del jugador 1"
            jugar = False
        else:
            pass

    def comprobarMatriz(self,x,y):
        if (TABLERO_2[x][y] is ""):
            return True
        else:
            return False

    def comprobarTriqui(self,jugador):
        #Primera coordenada en X, segunda coordenada en Y
        #Diagonal I-D
        if TABLERO_2[0][0]==TABLERO_2[1][1]==TABLERO_2[2][2]=="X" or TABLERO_2[0][0]==TABLERO_2[1][1]==TABLERO_2[2][2]=="O":
            return True
        #Diagonal D-I
        elif TABLERO_2[0][2]==TABLERO_2[1][1]==TABLERO_2[2][0]=="X" or TABLERO_2[0][2]==TABLERO_2[1][1]==TABLERO_2[2][0]=="O":
            return True
        #Columnas
        elif TABLERO_2[0][0]==TABLERO_2[0][1]==TABLERO_2[0][2]=="X" or TABLERO_2[0][0]==TABLERO_2[0][1]==TABLERO_2[0][2]=="O" :
            return True
        elif TABLERO_2[1][0]==TABLERO_2[1][1]==TABLERO_2[1][2]=="X" or TABLERO_2[1][0]==TABLERO_2[1][1]==TABLERO_2[1][2]=="O":
            return True
        elif TABLERO_2[2][0]==TABLERO_2[2][1]==TABLERO_2[2][2]=="X" or TABLERO_2[2][0]==TABLERO_2[2][1]==TABLERO_2[2][2]=="O":
            return True
        #Filas
        elif TABLERO_2[0][0]==TABLERO_2[1][0]==TABLERO_2[2][0]=="X" or TABLERO_2[0][0]==TABLERO_2[1][0]==TABLERO_2[2][0]=="O":
            return True
        elif TABLERO_2[0][1]==TABLERO_2[1][1]==TABLERO_2[2][1]=="X" or TABLERO_2[0][1]==TABLERO_2[1][1]==TABLERO_2[2][1]=="O":
            return True
        elif TABLERO_2[0][2]==TABLERO_2[1][2]==TABLERO_2[2][2]=="X" or TABLERO_2[0][1]==TABLERO_2[1][1]==TABLERO_2[2][1]=="O":
            return True
        else:
            return False



