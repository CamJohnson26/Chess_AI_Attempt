import time
from os.path import join

import chess
import chess.pgn
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def position_eval(fen, difficulties, debug):

    for difficulty in difficulties:
        white_player = ChessAi(evaluate_board_simple_count, difficulty)
        board = chess.Board()
        board.set_fen(fen)
        moves = white_player.rank_moves(board)
        print('--------------------------')
        print(f'Difficulty: {difficulty}')
        for move in moves:
            print(move)
        print(white_player.get_move(board))

if __name__ == '__main__':
    fen = '''
    
6nr/5k2/b3p1p1/7p/2P1P3/1P5P/1bp2PP1/2r2K1R w - - 0 39
    
    '''
    (position_eval(fen, [1, 3], False))
