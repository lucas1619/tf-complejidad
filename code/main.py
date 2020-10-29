from Quoridor import Quoridor
import matplotlib.pyplot as plt
def main():
    eleccion = int(input("1. Para testear los algoritmos, 2.- Para visualizar un juego: "))
    if eleccion == 1:
        algoritmos = [1,2,3]
        titulo = ["Bellman Ford", "Dijikstra", "A Star"]
        tiempos = [] #guarda los tiempos
        tam = [] #guarda los tamaños
        for i,algoritmo in enumerate(algoritmos):
            size = 5
            while(size <= 5000):
                game = Quoridor(size, 2)
                tiempos.append(game.test(algoritmo))
                tam.append(size)
                if(tiempos[len(tiempos) - 1] > 60000):
                    break
                if size < 10:
                    size += 5
                elif size < 100:
                    size +=10
                elif size < 1000:
                    size += 100
                else:
                    size += 500
            #hacer para que matplotlib genere el grafico
            plt.plot(tam, tiempos)
            plt.title(titulo[i], fontsize=22)
            plt.xlabel("Tamaño del tablero", fontsize=18)
            plt.ylabel("Tiempo en ms", fontsize=18)
            plt.show()
            #limpiamos
            tiempos.clear()
            tam.clear()
    else:
        board = 1
        while board < 3 or board > 50:
            board = int(input("Ingrese el tamaño del tablero mayor a 3  y menor a 50: "))
        game = Quoridor(board, 2)
        game.start()
main()