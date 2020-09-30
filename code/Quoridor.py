from Tablero import Tablero
from Jugador import Jugador
import pygame

blanco = (255, 255, 255)
colores = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)]


class Quoridor:
    def __init__(self, n, qjugadores):
        self.turno = 0
        self.tablero = Tablero(n)
        self.ganador = False
        self.lista_de_jugadores = []
        self.lista_de_jugadores.append(
            Jugador(2, self.tablero.grafo, self.tablero.n // 2, (self.tablero.q_nodos - self.tablero.n // 2) - 1))
        self.lista_de_jugadores.append(
            Jugador(1, self.tablero.grafo, (self.tablero.q_nodos - self.tablero.n // 2) - 1, self.tablero.n // 2))
        if qjugadores == 4:
            self.lista_de_jugadores.append(
                Jugador(1, self.tablero.grafo, (self.tablero.n * (self.tablero.n / 2 + 1)) - 1,
                        (self.tablero.n * (self.tablero.n / 2 + 1)) - self.tablero.n))
            self.lista_de_jugadores.append(
                Jugador(3, self.tablero.grafo, (self.tablero.n * (self.tablero.n / 2 + 1)) - self.tablero.n,
                        (self.tablero.n * (self.tablero.n / 2 + 1)) - 1))

    def start(self):
        pygame.init()
        pygame.display.set_caption(u'Quoridor')
        pantalla = pygame.display.set_mode((792, 792))
        clock = pygame.time.Clock()
        is_running = True
        pantalla.fill(blanco)
        self.tablero.graficar_tablero(pantalla, pygame)
        for i, jugador in enumerate(self.lista_de_jugadores):
            jugador.graficar(pantalla, pygame, self.tablero.n, self.tablero.tam, colores[i])
        pygame.display.update()
        pygame.time.wait(3000)
        while is_running:

            if self.ganador:
                break
            clock.tick(4)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            pantalla.fill(blanco)
            self.tablero.graficar_tablero(pantalla, pygame)
            for i, jugador in enumerate(self.lista_de_jugadores):
                jugador.graficar(pantalla, pygame, self.tablero.n, self.tablero.tam, colores[i])
            self.lista_de_jugadores[self.turno].piensa(self.lista_de_jugadores[(self.turno + 1) % 2], self.tablero)
            self.ganador = self.lista_de_jugadores[self.turno].mueve(self.lista_de_jugadores[(self.turno + 1) % 2],
                                                                     self.tablero)
            self.turno = (self.turno + 1) % 2
            pygame.display.update()

        pantalla.fill(blanco)
        self.tablero.graficar_tablero(pantalla, pygame)
        for i, jugador in enumerate(self.lista_de_jugadores):
            jugador.graficar(pantalla, pygame, self.tablero.n, self.tablero.tam, colores[i])
        pygame.display.update()
        pygame.time.wait(3000)

        pygame.quit()
