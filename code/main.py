from Game import Game
if __name__ == "__main__":
    players = int(input('Ingresa el numero de jugadores: '))
    board = int(input('Ingresa el tamaño del tablero: '))
    game = Game(players, board, False)
    time = game.play()
    print(time)
