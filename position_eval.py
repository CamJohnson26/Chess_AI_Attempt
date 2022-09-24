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

if __name__ == '__main__':
    fen = '''
    
r1bqkbnr/ppp1pp1p/n2p2p1/8/3P1P2/PP5N/2PKP1PP/RNBQ1B1R b HAkq - 0 1
    
    '''
    (position_eval(fen, [5], False))
