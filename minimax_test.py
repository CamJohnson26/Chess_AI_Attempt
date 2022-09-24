import time
from os.path import join

import chess
import chess.pgn
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def position_eval(fen, difficulty, debug=False):
    white_player = ChessAi(evaluate_board_simple_count, difficulty)
    board = chess.Board()
    board.set_fen(fen)
    sorted_moves = white_player.rank_moves(board)
    all_best_moves = [a for a in sorted_moves if a[0] == sorted_moves[0][0]]
    print([str(a[1]) for a in all_best_moves], all_best_moves[0][0])
    return all_best_moves[0]

if __name__ == '__main__':
    test_cases = [
        # # Black mate in 1
        # ('r3k1nr/ppp2pp1/5q1p/P2p4/3bp3/6P1/NPPPn3/R1BQKB1R b KQkq - 1 13', 1, -9999, ['f6f2']),
        # ('r3k1nr/ppp2pp1/5q1p/P2p4/3bp3/6P1/NPPPn3/R1BQKB1R b KQkq - 1 13', 3, -9999, ['f6f2']),
        # # Black mate in 2
        # ('r3k1nr/ppp2pp1/5q1p/P2p4/3bp3/6P1/NPPP4/R1B1KB2 b Qkq - 1 13', 2, -9997, ['f6f2']),
        # # White mate in 1
        # ('r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1', 1, 9999, ['f3f7']),
        # # White mate in 2
        # ('r1b1k1nr/pppp1ppp/2n5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1', 2, 9997, ['f3f7']),
        # Past Fail 1
        # ('r1bqkbnr/ppp1pp1p/n2p2p1/8/3P1P2/PP5N/2PKP1PP/RNBQ1B1R b HAkq - 0 1', 4, -1, ['c8h3', 'f8h6', 'g8f6', 'c8g4', 'f8g7', 'a6c5', 'e7e5', 'a6b8', 'c7c6', 'c7c5']),
        ('r2qkbnr/1p2p1pp/2np1p2/p1p5/2PP2b1/1P5N/P1NBPPPP/R2QKBR1 b Qkq - 0 9', 4, -2, ['c6d4', 'c5d4'])
    ]
    for test_case in test_cases:
        print(test_case)
        result = position_eval(test_case[0], test_case[1])
        print(result)
        assert str(result[1]) in test_case[3] and result[0] == test_case[2]
