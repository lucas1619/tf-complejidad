from Pensamiento import Pensamiento
class Jugador:
    def __init__(self, indica, Grafo, nodostart, nodogoal):
        self.nodogoal = nodogoal
        self.pensamiento = Pensamiento(Grafo, indica)
        self.lista_ruta = []
        self.current = nodostart

    def piensa(self):
        self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
        #lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)

    def mueve(self):
        self.current = self.lista_ruta[1]
        return self.current == self.nodogoal

    def graficar(self, pantalla, pygame, n, lado):
        x = self.current%n
        y = self.current//n
        pygame.draw.ellipse(pantalla, (100,100,100), (x*lado, y*lado, lado, lado), 0)

