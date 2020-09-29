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
    def piensa(self, rival):
        if self.primero:
            self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
            self.primero = False
        #self.lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)

    def mueve(self):
        self.current = self.lista_ruta[0]
        self.lista_ruta.pop(0)
        return self.current == self.nodogoal

    def graficar(self, pantalla, pygame, n, lado):
        x = self.current%n
        y = self.current//n
        x1 = self.nodogoal%n
        y1 = self.nodogoal//n
        if self.primero == False:
            pygame.draw.rect(pantalla, blue, (x1*lado, y1*lado, lado, lado), 0)
        pygame.draw.ellipse(pantalla, (100,100,100), (x*lado, y*lado, lado, lado), 0)
