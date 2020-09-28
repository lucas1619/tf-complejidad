from Tablero import Tablero
from Jugador import Jugador
import pygame
blanco = (255,255,255) 
class Quoridor:
    def __init__(self, n, qjugadores):
        self.turno = 0
        self.tablero = Tablero(n)
        self.ganador = False
        self.lista_de_jugadores = []
        self.lista_de_jugadores.append(
            Jugador(1, self.tablero.grafo, self.tablero.n // 2, (self.tablero.q_nodos - self.tablero.n // 2)))
        self.lista_de_jugadores.append(
            Jugador(1, self.tablero.grafo, (self.tablero.q_nodos - self.tablero.n // 2) - 1, self.tablero.n // 2))
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
    def start(self):
        pygame.init()
        pygame.display.set_caption(u'Jessie uwu')
        pantalla = pygame.display.set_mode((792, 792))
        clock = pygame.time.Clock()
        ganador = False
        is_running = True or ganador == False
        while is_running:
            clock.tick(7)
            for event in pygame.event.get():
                pantalla.fill(blanco)
                self.tablero.graficar_tablero(pantalla, pygame)
                for jugador in self.lista_de_jugadores:
                    jugador.graficar(pantalla, pygame, self.tablero.n, self.tablero.tam)
                    jugador.piensa()
                    ganador = jugador.mueve()
                    pygame.time.wait(100)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    is_running = False                    
        pygame.quit()        