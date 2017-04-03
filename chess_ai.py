import chess
from random import randint


class ChessAi:

    def __init__(self):
        pass

    def get_move(self, board):
        avail_moves = board.legal_moves
        return list(avail_moves)[randint(0, len(list(avail_moves)) - 1)]
