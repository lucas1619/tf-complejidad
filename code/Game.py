from Board import Board
from Player import Player
from algorithms import astar, dijkstra, bellman_ford
import networkx as nx
import pygame, sys
from pygame.locals import *
import time

strategies = [astar, bellman_ford, dijkstra]


class Game:
    def __init__(self, n_players, size, graphic=None, max_depth=4, strats=[]):
        self.max_deth = max_depth
        self.board = Board(size)
        self.players = [None] * n_players
        self.graphic = size <= 18 if graphic is None else graphic
        key_pos1 = size // 2
        key_pos2 = (size // 2) * size
        if len(self.players) == 2:
            if not strats:
                strats = [0, 1]
            self.players[0] = Player(strategies[strats[0]], key_pos1, key_pos1 + (size * (size - 1)), 1, (0, 0, 255))
            self.players[1] = Player(strategies[strats[1]], key_pos1 + (size * (size - 1)), key_pos1, 1, (0, 255, 0))
        elif len(self.players) == 4:
            if not strats:
                strats = [0, 1, 2, 1]
            self.players[0] = Player(strategies[strats[0]], key_pos1, key_pos1 + (size * (size - 1)), 1, (0, 0, 255))
            self.players[1] = Player(strategies[strats[1]], key_pos1 + (size * (size - 1)), key_pos1, 1, (0, 255, 0))
            self.players[2] = Player(strategies[strats[2]], key_pos2, key_pos2 + (size - 1), 1, (0, 0, 0))
            self.players[3] = Player(strategies[strats[3]], key_pos2 + (size - 1), key_pos2, 1, (255, 255, 255))
        for player in self.players:
            if size % 2 == 0:
                player.walls = size / len(self.players)
            else:
                player.walls = (size + 1) / len(self.players)

    def evaluate_position(self, player, players, board):
        if player.is_winner():
            return float('inf')
        score = len(player.path_find(board))
        for p in players:
            if p != player:
                score -= len(p.path_find(board))
        return score

    def validate_direction(self, start_node, end_node):
        validate = start_node - end_node
        if validate == self.board.size:
            return 0  # arriba a abajo
        elif validate == -self.board.size:
            return 1  # arriba a abajo
        elif validate == -1:
            return 2  # izquierda a derecha
        elif validate == 1:
            return 3  # derecha a izquierda

    def get_coord(self, nodo, size, width_square):
        x = nodo % size
        y = nodo // size
        x = x * width_square + 3 * x
        y = y * width_square + 3 * y
        return [x, y]

    def offensive_wall(self, objective_player, board, players, real_wall=False):
        if real_wall == False:
            it_could = True
            for i in range(len(objective_player.path_find(board.G)) - 1):
                indicator = self.validate_direction(objective_player.path_find(board.G)[i],
                                                    objective_player.path_find(board.G)[i + 1])
                # 0 arriba, 1 abajo, 2 derecha, 3 izquierda
                if indicator == 0:
                    if board.add_wall(objective_player.path_find(board.G)[i],
                                      objective_player.path_find(board.G)[i] - self.board.size,
                                      objective_player.path_find(board.G)[i] + 1,
                                      objective_player.path_find(board.G)[i] - self.board.size + 1, players):
                        break
                    else:
                        continue
                elif indicator == 1:
                    if board.add_wall(objective_player.path_find(board.G)[i],
                                      objective_player.path_find(board.G)[i] + self.board.size,
                                      objective_player.path_find(board.G)[i] + 1,
                                      objective_player.path_find(board.G)[i] + self.board.size + 1, players):
                        break
                    else:
                        continue
                elif indicator == 2:
                    if board.add_wall(objective_player.path_find(board.G)[i],
                                      objective_player.path_find(board.G)[i] + 1,
                                      objective_player.path_find(board.G)[i] + self.board.size,
                                      objective_player.path_find(board.G)[i] + self.board.size + 1, players):
                        break
                    else:
                        continue
                elif indicator == 3:
                    if board.add_wall(objective_player.path_find(board.G)[i],
                                      objective_player.path_find(board.G)[i] - 1,
                                      objective_player.path_find(board.G)[i] + self.board.size,
                                      objective_player.path_find(board.G)[i] + self.board.size - 1, players):
                        break
                    else:
                        continue
                if i == len(objective_player.path_find(board.G)) - 2:
                    # no se pudo poner pared
                    it_could = False
            return it_could
        else:
            it_could = True
            for i in range(len(objective_player.path_find(board.G)) - 1):
                indicator = self.validate_direction(objective_player.path_find(board.G)[i],
                                                    objective_player.path_find(board.G)[i + 1])
                # 0 arriba, 1 abajo, 2 derecha, 3 izquierda
                if indicator == 0:
                    if self.board.add_wall(objective_player.path_find(self.board.G)[i],
                                           objective_player.path_find(self.board.G)[i] - self.board.size,
                                           objective_player.path_find(self.board.G)[i] + 1,
                                           objective_player.path_find(self.board.G)[i] - self.board.size + 1, players):
                        break
                    else:
                        continue
                elif indicator == 1:
                    if self.board.add_wall(objective_player.path_find(self.board.G)[i],
                                           objective_player.path_find(self.board.G)[i] + self.board.size,
                                           objective_player.path_find(self.board.G)[i] + 1,
                                           objective_player.path_find(self.board.G)[i] + self.board.size + 1, players):
                        break
                    else:
                        continue
                elif indicator == 2:
                    if self.board.add_wall(objective_player.path_find(self.board.G)[i],
                                           objective_player.path_find(self.board.G)[i] + 1,
                                           objective_player.path_find(self.board.G)[i] + self.board.size,
                                           objective_player.path_find(self.board.G)[i] + self.board.size + 1, players):
                        break
                    else:
                        continue
                elif indicator == 3:
                    if self.board.add_wall(objective_player.path_find(self.board.G)[i],
                                           objective_player.path_find(self.board.G)[i] - 1,
                                           objective_player.path_find(self.board.G)[i] + self.board.size,
                                           objective_player.path_find(self.board.G)[i] + self.board.size - 1, players):
                        break
                    else:
                        continue
                if i == len(objective_player.path_find(self.board.G)) - 2:
                    # no se pudo poner pared
                    it_could = False
            return it_could

    def deffensive_wall(self, objective_player: Player, board):
        print('deffensive_wall')

    def play(self):
        start = time.time()
        winner_id = None
        turn = 0
        best_score = None
        score = None
        if self.graphic:
            """parte grafica aca"""
            pygame.init()
            window = pygame.display.set_mode((800, 800))
            pygame.display.set_caption('Quoridor')
            clock = pygame.time.Clock()
            width_square = 800 // (self.board.size + 1)
            coords = []
            first_adjacency_list = dict(self.board.G.copy().adjacency())
            """fin parte grafica aca"""
        while 1:
            if self.graphic:
                """parte grafica aca"""
                actual_adjacency_list = dict(self.board.G.adjacency())
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit(1)
                window.fill((90, 50, 15))
                for node in list(self.board.G):
                    coords = self.get_coord(node, self.board.size, width_square)
                    pygame.draw.rect(window, (255, 0, 0), [coords[0], coords[1], width_square, width_square], 0)
                    if first_adjacency_list[node] != actual_adjacency_list[node]:
                        for element in first_adjacency_list[node]:
                            if element not in actual_adjacency_list[node]:
                                direction = node - element
                                if direction == -self.board.size:  # abajo
                                    pygame.draw.rect(window, (255, 255, 0),
                                                     [coords[0], coords[1] + width_square, width_square, 3], 0)
                                elif direction == self.board.size:  # arriba
                                    pygame.draw.rect(window, (255, 255, 0), [coords[0], coords[1] - 3, width_square, 3],
                                                     0)
                                elif direction == -1:  # derecha
                                    pygame.draw.rect(window, (255, 255, 0),
                                                     [coords[0] + width_square, coords[1], 3, width_square], 0)
                                elif direction == 1:  # izquierda
                                    pygame.draw.rect(window, (255, 255, 0), [coords[0] - 3, coords[1], 3, width_square],
                                                     0)
                for player in self.players:
                    coords = self.get_coord(player.current, self.board.size, width_square)
                    pygame.draw.ellipse(window, player.color, [coords[0], coords[1], width_square, width_square], 0)
                """fin parte grafica aca"""
            max_score = float('-inf')
            before_current = self.players[turn].current
            before_board = self.board.copy()
            movement = {'type': 'm', 'target': -1}
            # Primero es mover
            self.players[turn].move_pawn(self.board.G)
            score = self.paranoid(self.board, 1, (turn + 1) % len(self.players), self.players.copy())
            max_score = max(score, max_score)
            self.players[turn].current = before_current
            if self.players[turn].has_walls():
                for i, p in enumerate(self.players):
                    if i != turn:
                        if self.players[turn].wall_strategy == 1:
                            self.offensive_wall(p, self.board, self.players)
                            self.players[turn].walls -= 1
                        score = self.paranoid(self.board, 1, (turn + 1) % len(self.players), self.players.copy())
                        if score > max_score:
                            movement['type'] = 'w'
                            movement['target'] = i
                        self.board = before_board
                        self.players[turn].walls += 1
            if movement['type'] == 'm':
                self.players[turn].move_pawn(self.board.G, True)
                for i, p in enumerate(self.players):
                    if i != turn:
                        if p.current == self.players[turn].current:
                            self.players[turn].move_pawn(self.board.G, True)
            else:
                if self.players[turn].wall_strategy == 1:
                    self.offensive_wall(self.players[movement['target']], self.board, self.players)
                self.players[turn].walls -= 1
            if self.players[turn].is_winner():
                winner_id = turn
                break
            turn = (turn + 1) % len(self.players)
            if self.graphic:
                pygame.display.flip()
                clock.tick(1)
        print(f'The winner is the player {winner_id + 1}')
        end = time.time()
        return end - start

    def paranoid(self, board, depth, player, players):
        if depth == len(players) * self.max_deth:
            return self.evaluate_position(players[player], players, board.G)
        if depth % len(self.players) == 0:
            max_score = float('-inf')
            before_current = players[player].current
            before_board = board.copy()
            # Primero es mover
            players[player].move_pawn(board.G)
            score = self.paranoid(board, depth + 1, (player + 1) % len(players), players)
            max_score = max(score, max_score)
            players[player].current = before_current
            for i, p in enumerate(players):
                if i != player:
                    if players[player].wall_strategy == 1:
                        self.offensive_wall(p, board, players)
                        players[player].walls -= 1
                    score = self.paranoid(board.copy(), depth + 1, (player + 1) % len(players), players)
                    max_score = max(score, max_score)
                    board = before_board
                    players[player].walls += 1
            return max_score
        else:
            min_score = float('inf')
            before_current = players[player].current
            before_board = board.copy()
            # Primero es mover
            players[player].move_pawn(board.G)
            score = self.paranoid(board, depth + 1, (player + 1) % len(players), players)
            min_score = min(score, min_score)
            players[player].current = before_current
            for i, p in enumerate(players):
                if i != player:
                    if players[player].wall_strategy == 1:
                        self.offensive_wall(p, board, players, True)
                        players[player].walls -= 1
                    score = self.paranoid(board.copy(), depth + 1, (player + 1) % len(players), players)
                    min_score = min(score, min_score)
                    board = before_board
                    players[player].walls += 1
            return min_score
