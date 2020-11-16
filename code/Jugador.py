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

    def poner_pared_bri(self, enemigo, tablero):

        #hacer que la pared haga la ruta mas largas
        #comparo el tamaño de las rutas que tomara si rompo algun nodo
        #elijo la mayor ruta, veo si esos 4 nodos están conectados
        #si estan conectados y si hay una posible ruta desde donde esta el enemigo hasta la meta
        #aunque lo de arriba ya se probaria en el 2do paso al comparar rutas
        # rompo la conexion y sigo
        # tengo que ver como evaluo cuando una ruta no es posible
        def condicion(nodo1, nodo2, nodo3, nodo4, enemigo, indica = 0):
            #falta ver lo que devolverian las rutas si no hay camino a ese nodo
            if indica == 1:
                self.grafo.eliminar_nodo(nodo1, nodo2)
                self.grafo.eliminar_nodo(nodo3, nodo4)
                return 
            if self.grafo.conectados(nodo1, nodo2) and self.grafo.conectados(nodo3, nodo4):
                self.grafo.eliminar_nodo(nodo1, nodo2)
                self.grafo.eliminar_nodo(nodo3, nodo4)
                lista_ruta = enemigo.pensamiento.actualiza_ruta(enemigo.current, enemigo.nodogoal)
                self.grafo.crear_conexion(nodo1, nodo2)
                self.grafo.crear_conexion(nodo3, nodo4)
                return lista_ruta
            else: return [1]*float("inf")
        
        listas_de_rutas = []
        listas_de_nodos = [
            [enemigo.current, enemigo.current + self.grafo.n, enemigo.current+1, enemigo.current + 1+self.grafo.n],
            [enemigo.current, enemigo.current + self.grafo.n, enemigo.current-1, enemigo.current-1+self.grafo.n],
            [enemigo.current, enemigo.current - self.grafo.n, enemigo.current+1, enemigo.current + 1 - self.grafo.n],
            [enemigo.current, enemigo.current - self.grafo.n, enemigo.current-1, enemigo.current - 1 - self.grafo.n],
            [enemigo.current, enemigo.current-1, enemigo.current + self.grafo.n, enemigo.current + self.grafo.n - 1],
            [enemigo.current, enemigo.current-1, enemigo.current - self.grafo.n, enemigo.current - self.grafo.n - 1],
            [enemigo.current, enemigo.current + 1, enemigo.current - self.grafo.n, enemigo.current - self.grafo.n + 1],
            [enemigo.current, enemigo.current + 1, enemigo.current + self.grafo.n, enemigo.current + self.grafo.n + 1]]
        
        for lista in listas_de_nodos:
            listas_de_rutas.append(condicion(lista[0], lista[1], lista[2], lista[3], enemigo))

        x = 1
        for enume, j in enumerate(listas_de_rutas):
            if len(j) > x:
                x = len(j)
                indice = enume
        
        condicion(listas_de_nodos[indice][0], listas_de_nodos[indice][1], listas_de_nodos[indice][2], listas_de_nodos[indice][3], enemigo, 1)

    def obtiene_current_anterior(self, enemigo):
        global enemigo_current_anterior
        enemigo_current_anterior = enemigo.current

    def poner_pared_lucas(self, enemigo, tablero):
        # ya no haya sido puesta, validar :v por si ya no hay algo ahi
        global enemigo_current_anterior
        n_grafo = self.grafo.n

        if enemigo_current_anterior - n_grafo == enemigo.current: #me movi arriba
            nodo1, nodo2, nodo3, nodo4 = self.current, self.current -n_grafo, self.current +1, (self.current -n_grafo)+1
            if self.grafo.colocar_pared(nodo1, nodo2, nodo3, nodo4):
                return
            else:
                for i in range(1,4):            
                    if self.grafo.conectados(self.current - (n_grafo*i), self.current-(n_grafo*(i+1))) and self.grafo.conectados((self.current - (n_grafo*i))+1, self.current-(n_grafo*(i+1))+1):
                        self.grafo.eliminar_nodo(self.current - (n_grafo*i), self.current-(n_grafo*(i+1))) 
                        self.grafo.eliminar_nodo((self.current - (n_grafo*i))+1, self.current-(n_grafo*(i+1))+1)
                        break
                    if i == 3:
                        return -1
                return

        elif enemigo_current_anterior + n_grafo == enemigo.current:#me movi abajo
            nodo1, nodo2, nodo3, nodo4 = self.current, self.current + n_grafo, self.current + 1, (self.current +n_grafo)+1
            if self.grafo.colocar_pared(nodo1, nodo2, nodo3, nodo4):
                return True
            else:
                for i in range(1,4):            
                    if self.grafo.conectados(self.current + (n_grafo*i), self.current+(n_grafo*(i+1))) and self.grafo.conectados((self.current + (n_grafo*i))+1, self.current+(n_grafo*(i+1))+1):
                        self.grafo.eliminar_nodo(self.current + (n_grafo*i), self.current+(n_grafo*(i+1))) 
                        self.grafo.eliminar_nodo((self.current + (n_grafo*i))+1, self.current+(n_grafo*(i+1))+1)
                        break
                    if i == 3:
                        return -1
                return


        elif enemigo_current_anterior - 1 == enemigo.current:#me movi izquierda
            nodo1, nodo2, nodo3, nodo4 = self.current, self.current-1, self.current - n_grafo , (self.current- n_grafo)-1
            if self.grafo.colocar_pared(nodo1, nodo2, nodo3, nodo4):
                return True
            else:
                for i in range(1,4):
                    if self.grafo.conectados(self.current - (1*i) , self.current - (1*i) -1 ) and self.grafo.conectados(self.current - (1*i) - n_grafo , self.current - (1*i) -1 - n_grafo):
                        break
            



        elif enemigo_current_anterior + 1 == enemigo.current:#me movi derecha
            nodo1, nodo2, nodo3, nodo4 = self.current, self.current+1, self.current - n_grafo, (self.current-n_grafo)+1
            if self.grafo.colocar_pared(nodo1, nodo2, nodo3, nodo4):
                return True
        #si no le puedo poner pared en un lugar, le pongo a la siguiente fila o columna
        #si ya no se puede, avanzo



        
        


        
        
        










        


    def graficar(self, pantalla, pygame, n, lado, color):
        x = self.current % n
        y = self.current // n
        x1 = self.nodogoal % n
        y1 = self.nodogoal // n
        pygame.draw.ellipse(pantalla, color, (x * lado, y * lado, lado, lado), 0)
