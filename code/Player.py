class Player:
    def __init__(self, path_finder, start, goal, wall_strategy, color):
        self.current = start
        self.goal = goal
        self.walls = None
        self.path_finder = path_finder
        self.wall_strategy = wall_strategy
        self.color = color

    def path_find(self, board):
        try:
            lista = self.path_finder(board, self.current, self.goal)
            return lista
        except:
            return []

    def is_winner(self):
        return self.goal == self.current

    def has_walls(self):
        return self.walls > 0

    def move_pawn(self, board, is_real_move=False):
        if len(self.path_find(board)) == 1:
            self.current = self.goal
        else:
            self.current = self.path_find(board)[1]