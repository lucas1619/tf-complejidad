from Game import Game
if __name__ == "__main__":
    decision = int(input('Selecciona 1 si deseas testear y 2 si deseas visualizar: '))
    if decision == 1:
        algoritmos = ['A Star', 'Bellman Ford', 'Dijkstra']
        profundidades = [1, 2, 3]
        tamanhos = [4, 5, 10, 20, 30]
        for profundidad in profundidades:
            for algoritmo in range(3):
                for tamanho in tamanhos:
                    print(tamanho, profundidad, algoritmos[algoritmo])
                    game = Game(2, tamanho, False, profundidad, [algoritmo, algoritmo])
                    time = game.play()
                    print(time)
    elif decision == 2:
        players = int(input('Ingresa el numero de jugadores: '))
        board = int(input('Ingresa el tamaño del tablero menor a 18: '))
        game = Game(players, board, True)
        time = game.play()
        print(time)
