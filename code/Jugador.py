from Pensamiento import Pensamiento
blue = (95, 158, 160)
class Jugador:
    def __init__(self, indica, Grafo, nodostart, nodogoal):
        self.nodogoal = nodogoal
        self.pensamiento = Pensamiento(Grafo, indica)
        self.lista_ruta = []
        self.lista_ruta_rival = []
        self.current = nodostart
        self.primero = True
        self.grafo = Grafo
        global enemigo_current_anterior

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
        if self.current == rival.nodogoal and self.primero == False:
            self.lista_ruta = [self.current - 1]
            return
        if self.lista_ruta == []:
            self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
            return
        if len(self.lista_ruta) < len(self.lista_ruta_rival):
            return
        if self.alcostado(self.current, rival.current, tablero.n) is True:
            self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, rival.nodogoal)
            return
        if self.alcostado(self.lista_ruta[0], rival.current, tablero.n) is True:
            self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, rival.nodogoal)
            return

    def alcostado(self, nodo1, nodo2, n):
        return nodo1 - 1 is nodo2 or nodo1 + 1 is nodo2 or nodo1 + n is nodo2 or nodo1 - n is nodo2

    def validar_direccion(self, nodoI, nodoF, n):
        validar = nodoI - nodoF
        if (validar == n):
            return 0  # arriba a abajo
        elif (validar == -n):
            return 1  # arriba a abajo
        elif (validar == -1):
            return 2  # izquierda a derecha
        elif (validar == 1):
            return 3  # derecha a izquierda

    def mueve(self, enemigo, tablero):
        inicial = self.current
        self.current = self.lista_ruta[0]
        self.lista_ruta.pop(0)
        if self.current == enemigo.current:
            direccion = self.validar_direccion(inicial, self.current, tablero.n)
            if direccion == 0:
                if self.current - tablero.n >= 0:
                    if tablero.conectados(self.current, self.current - tablero.n):
                        self.current -= tablero.n
                    else:
                        pass
                else:
                    self.current += 1
                    self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
                    return self.current == self.nodogoal
            elif direccion == 1:
                if self.current + tablero.n < tablero.n:
                    if tablero.conectados(self.current, self.current + tablero.n):
                        self.current += tablero.n
                    else:
                        pass
                else:
                    self.current += 1
                    self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
                    return self.current == self.nodogoal
            elif direccion == 2:
                if tablero.conectados(self.current, self.current + 1):
                    self.current += 1
                else:
                    pass
            elif direccion == 3:
                if tablero.conectados(self.current, self.current - 1):
                    self.current -= 1
                else:
                    pass
            if self.current == self.lista_ruta[0]:
                self.lista_ruta.pop(0)
            else:
                self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
        return self.current == self.nodogoal


        def ofensivo(self, enemigo):
            se_pudo = True
            for i in range(len(enemigo.lista_ruta)-1):
                indicador = self.validar_direccion(enemigo.lista[i],enemigo.lista[i+1], self.grafo.n)
            # 0 arriba, 1 abajo, 2 derecha, 3 izquierda
                if indicador == 0:
                    if (self.grafo.colocar_pared(enemigo.lista[i],enemigo.lista[i]-self.grafo.n,enemigo.lista[i]+1,enemigo.lista[i]-self.grafo.n +1)):
                        break
                    else:
                        continue
                elif indicador == 1:
                    if (self.grafo.colocar_pared(enemigo.lista[i],enemigo.lista[i]+self.grafo.n,enemigo.lista[i]+1,enemigo.lista[i]+self.grafo.n +1)):
                        break
                    else:
                        continue
                elif indicador == 2:
                    if (self.grafo.colocar_pared(enemigo.lista[i],enemigo.lista[i]+1,enemigo.lista[i]+self.grafo.n, enemigo.lista[i]+self.grafo.n+1)):
                        break
                    else:
                        continue
                elif indicador == 3:
                    if (self.grafo.colocar_pared(enemigo.lista[i],enemigo.lista[i]-1,enemigo.lista[i]+self.grafo.n, enemigo.lista[i]+self.grafo.n-1)):
                        break
                    else:
                        continue
                if i == len(enemigo.lista_ruta)-1:
                    #no se pudo poner pared
                    se_pudo = False
            return se_pudo



        
        


        
        
        










        


    def graficar(self, pantalla, pygame, n, lado, color):
        x = self.current % n
        y = self.current // n
        x1 = self.nodogoal % n
        y1 = self.nodogoal // n
        pygame.draw.ellipse(pantalla, color, (x * lado, y * lado, lado, lado), 0)
