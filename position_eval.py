import time
from os.path import join

import chess
import chess.pgn
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def position_eval(fen, debug):

    white_player = ChessAi(evaluate_board_simple_count, 5)
    board = chess.Board()
    board.set_fen(fen)
    moves = white_player.rank_moves(board)
    for move in moves:
        print(move)
    print(white_player.get_move(board))
    white_difficulty = 2
    # black_difficulty = 4
    # # random_ai = ChessAi(evaluate_board_random, 0)
    # # count_ai_1 = ChessAi(evaluate_board_simple_count, 1)
    # white_player = ChessAi(evaluate_board_simple_count, white_difficulty)
    # # count_ai_3 = ChessAi(evaluate_board_simple_count, 3)
    # black_player = ChessAi(evaluate_board_simple_count, black_difficulty)
    # # count_ai_5 = ChessAi(evaluate_board_simple_count, 5)
    # # count_ai_6 = ChessAi(evaluate_board_simple_count, 6)
    # board = chess.Board()
    # game = chess.pgn.Game()
    # event = f"Cameron Chess AI- {time.time()}"
    # game.headers["Event"] = event
    # game.headers["White"] = str(white_player) + '-' + str(white_difficulty)
    # game.headers["Black"] = str(black_player) + '-' + str(black_difficulty)
    # node = None
    # white_to_move = True
    # move_counter = 0
    # while not board.is_game_over():
    #     if debug:
    #         print(white_to_move)
    #         print("%s\n" % board)
    #     if white_to_move:
    #         next_move = white_player.get_move(chess.WHITE, board)
    #     else:
    #         next_move = black_player.get_move(chess.BLACK, board)
    #     if next_move in board.legal_moves:
    #         move_counter += 1
    #         if node is None:
    #             node = game.add_main_variation(next_move)
    #         else:
    #             node = node.add_main_variation(next_move)
    #         board.push(next_move)
    #         white_to_move = not white_to_move
    # if board.is_checkmate():
    #     if debug:
    #         print("Black wins!" if white_to_move else "White wins!")
    # else:
    #     if debug:
    #         print("It's a Draw!")
    # print("%s moves total" % board.fullmove_number)
    # print('\n\n')
    # with open(join('game_results', f"{event}.pgn")) as f:
    #     f.write(game)
    # return game

if __name__ == '__main__':
    (position_eval('rnQ5/1p3k2/7p/2p5/P2q1P2/1pn3r1/R2P4/2B1K3 b - - 3 41', False))
