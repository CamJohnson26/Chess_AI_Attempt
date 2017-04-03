import chess
from random import randint, shuffle


class ChessAi:

    def __init__(self):
        pass

    def get_move(self, board):
        moves = self.evaluate_board_random(board)
        return moves[0]

    def evaluate_board_random(self, board):
        moves = list(board.legal_moves)
        shuffle(moves)
        return moves

    def evaluate_board_simple_count(self, board):
        moves = list(board.legal_moves)
        return moves
