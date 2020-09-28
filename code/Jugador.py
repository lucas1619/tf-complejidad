from Pensamiento import Pensamiento
class Jugador:
    def __init__(self, indica, Grafo, nodostart, nodogoal):
        self.nodogoal = nodogoal
        self.pensamiento = Pensamiento(Grafo, indica)
        self.lista_ruta = []
        self.current = nodostart

    def piensa(self, rival):
        self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
        lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)

    def mueve(self):
        self.current = self.lista_ruta[0]
        return self.current == self.nodogoal
