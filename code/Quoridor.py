import Tablero
import Jugador


class Quoridor:
    def __init__(self, n, qjugadores):
        self.turno = 0
        self.tablero = Tablero(n)
        self.ganador = False
        self.lista_de_jugadores = []
        self.lista_de_jugadores.append(
            Jugador(1, self.tablero.grafo, self.tablero.n / 2, (self.tablero.q_nodos - self.tablero.n / 2)))
        self.lista_de_jugadores.append(
            Jugador(2, self.tablero.grafo, (self.tablero.q_nodos - self.tablero.n / 2), self.tablero.n / 2))
        if qjugadores == 4:
            self.lista_de_jugadores.append(
                Jugador(1, self.tablero.grafo, (self.tablero.n * (self.tablero.n / 2 + 1)) - 1,
                        (self.tablero.n * (self.tablero.n / 2 + 1)) - self.tablero.n))
            self.lista_de_jugadores.append(
                Jugador(3, self.tablero.grafo, (self.tablero.n * (self.tablero.n / 2 + 1)) - self.tablero.n,
                        (self.tablero.n * (self.tablero.n / 2 + 1)) - 1))

    def juguemos(self):
        while not self.ganador:
            self.lista_de_jugadores[self.turno].piensa(self.lista_de_jugadores[(self.turno + 1) % 2])
            self.ganador = self.lista_de_jugadores[self.turno].mueve()
            self.turno = (self.turno + 1) % 2
