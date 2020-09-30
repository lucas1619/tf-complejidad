from Pensamiento import Pensamiento
blue = (95,158,160)
class Jugador:
    def __init__(self, indica, Grafo, nodostart, nodogoal):
        self.nodogoal = nodogoal
        self.pensamiento = Pensamiento(Grafo, indica)
        self.lista_ruta = []
        self.lista_ruta_rival = []
        self.current = nodostart
        self.primero = True    
    def piensa(self, rival, tablero):
        if self.primero:
            self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
            self.lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)
            self.primero = False
            return
        
        if rival.current == self.lista_ruta_rival[0]:
            self.lista_ruta_rival.pop(0)
        else:
            self.lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)
        if len(self.lista_ruta) < len(rival.lista_ruta):
                return
        else:
            print("nos van a ganar :c")
            if self.nodogoal == (tablero.q_nodos - tablero.n // 2):
                self.lista_ruta.insert(0,self.current - tablero.n)
            else:
                self.lista_ruta.insert(0,self.current + tablero.n)    
    def validar_direccion(self, nodoI, nodoF, n):
        validar = nodoI-nodoF
        if (validar == n):
            return 0 #arriba a abajo
        elif (validar == -n):
            return  1 # arriba a abajo
        elif (validar == -1):
            return 2 #izquierda a derecha
        elif (validar == 1):
            return 3 #derecha a izquierda

    def mueve(self, enemigo, tablero):
        inicial = self.current
        self.current = self.lista_ruta[0]
        self.lista_ruta.pop(0)
        if self.current == enemigo.current:
            direccion = self.validar_direccion(inicial, self.current, tablero.n)
            if direccion is 0:
                if tablero.conectados(self.current, self.current - tablero.n):
                    self.current -= tablero.n
                else:
                    pass    
            elif direccion is 1:
                if tablero.conectados(self.current, self.current + tablero.n):
                    self.current += tablero.n
                else:
                    pass    
            elif direccion is 2:
                if tablero.conectados(self.current, self.current + 1):
                    self.current += 1
                else:
                    pass    
            elif direccion is 3:
                if tablero.conectados(self.current, self.current - 1):
                    self.current -= 1
                else:
                    pass                
        return self.current == self.nodogoal

    def graficar(self, pantalla, pygame, n, lado):
        x = self.current%n
        y = self.current//n
        x1 = self.nodogoal%n
        y1 = self.nodogoal//n
        if self.primero == False:
            pygame.draw.rect(pantalla, blue, (x1*lado, y1*lado, lado, lado), 0)
        pygame.draw.ellipse(pantalla, (100,100,100), (x*lado, y*lado, lado, lado), 0)
