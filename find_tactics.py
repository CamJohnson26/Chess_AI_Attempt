import time
from os.path import join

import chess
import chess.pgn
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def find_tactics(lower_difficulty, higher_difficulty, game):

    lower_player = ChessAi(evaluate_board_simple_count, lower_difficulty)
    higher_player = ChessAi(evaluate_board_simple_count, higher_difficulty)

    cur_node = game.end()
    while cur_node.parent is not None:
        prev_node = cur_node.parent
        cur_move = str(cur_node.move)
        board = prev_node.board()
        weak_evals = lower_player.rank_moves(board)
        high_evals = higher_player.rank_moves(board)

        weak_eval = [move for move in weak_evals if move[1] == cur_move][0][0]
        high_eval = [move for move in high_evals if move[1] == cur_move][0][0]

        difference = high_eval - weak_eval
        if difference > 1:
            if board.turn == 1:
                high_eval = high_eval * -1
                weak_eval = weak_eval * -1
            winning_by_more = high_eval > 0 and weak_eval > 0 and high_eval > weak_eval
            losing_by_more = high_eval < 0 and weak_eval < 0 and high_eval < weak_eval
            winning_by_less = high_eval > 0 and weak_eval > 0 and high_eval < weak_eval
            losing_by_less = high_eval < 0 and weak_eval < 0 and high_eval > weak_eval
            actually_winning = high_eval > 0 and weak_eval <= 0
            actually_losing = high_eval < 0 and weak_eval >= 0
            actually_tied = high_eval == 0 and not weak_eval == 0
            board.push(cur_node.move)

            print(board.fen(), ' Difference: ', difference)
            print(high_eval, weak_eval, cur_move)
            print(winning_by_more and 'Winning by More')
            print(losing_by_more and 'Losing by More')
            print(winning_by_less and 'Winning by Less')
            print(losing_by_less and 'Losing by Less')
            print(actually_winning and 'Actually Winning')
            print(actually_losing and 'Actually Losing')
            print(actually_tied and 'Actually Tied')
        cur_node = prev_node

if __name__ == '__main__':
    game_name = 'Cameron Chess AI- 1663889481.4459834.pgn'
    game = chess.pgn.read_game(open(join('game_results', game_name)))
    find_tactics(2, 4, game)
