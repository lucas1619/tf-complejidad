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
        if self.primero == False:
            print(f"actual {self.current}")
            print(f"yo {self.lista_ruta} ")
            print(f"rival {self.lista_ruta_rival} ")
        if self.current == rival.nodogoal and self.primero == False:
              self.lista_ruta = [self.current-1]   
              return
        if self.primero:
            self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)
            self.lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)
            self.primero = False
            return
        if self.lista_ruta == []:
           print("olah")
           self.lista_ruta = self.pensamiento.actualiza_ruta(self.current, self.nodogoal)    
           print(f"nueva ruta{self.lista_ruta}")
           return

        if rival.current == self.lista_ruta_rival[0]:
            self.lista_ruta_rival.pop(0)
        else:
            self.lista_ruta_rival = self.pensamiento.actualiza_ruta(rival.current, rival.nodogoal)
        if len(self.lista_ruta) < len(rival.lista_ruta):
                return
        else:
            if self.alcostado(self.lista_ruta[0],rival.current, tablero.n) is True:
                
                self.lista_ruta = self.pensamiento.actualiza_ruta(self.current,rival.nodogoal)
                print(self.lista_ruta)
                return
             
    def alcostado(self,nodo1,nodo2,n):
        return nodo1-1 is nodo2 or nodo1+1 is nodo2 or nodo1+n is nodo2 or nodo1-n is nodo2

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
            if self.current == self.lista_ruta[0]:
                self.lista_ruta.pop(0)
            else:
                self.lista_ruta = self.pensamiento.actualiza_ruta(self.current,self.nodogoal)
        print(self.current)        
        return self.current == self.nodogoal

    def graficar(self, pantalla, pygame, n, lado,color):
        x = self.current%n
        y = self.current//n
        x1 = self.nodogoal%n
        y1 = self.nodogoal//n
        if self.primero == False:
            pygame.draw.rect(pantalla, blue, (x1*lado, y1*lado, lado, lado), 0)
        pygame.draw.ellipse(pantalla, color, (x*lado, y*lado, lado, lado), 0)
