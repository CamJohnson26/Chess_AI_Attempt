import time
from os.path import join

import chess
import chess.pgn
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def play_game(debug, fen=None):

    white_difficulty = 2
    black_difficulty = 4
    # random_ai = ChessAi(evaluate_board_random, 0)
    # count_ai_1 = ChessAi(evaluate_board_simple_count, 1)
    white_player = ChessAi(evaluate_board_simple_count, white_difficulty)
    # count_ai_3 = ChessAi(evaluate_board_simple_count, 3)
    black_player = ChessAi(evaluate_board_simple_count, black_difficulty)
    # count_ai_5 = ChessAi(evaluate_board_simple_count, 5)
    # count_ai_6 = ChessAi(evaluate_board_simple_count, 6)
    board = chess.Board()
    game = chess.pgn.Game()
    if fen is not None:
        board.set_fen(fen)
        game.setup(board)
    event = f"Cameron Chess AI- {time.time()}"
    game.headers["Event"] = event
    game.headers["White"] = str(white_player) + '-' + str(white_difficulty)
    game.headers["Black"] = str(black_player) + '-' + str(black_difficulty)
    node = None
    white_to_move = True
    move_counter = 0
    while not board.is_game_over():
        if debug:
            print(white_to_move)
            print("%s\n" % board)
        if white_to_move:
            next_move = get_move_from_string(white_player.get_move(board), board)
        else:
            next_move = get_move_from_string(black_player.get_move(board), board)
        if next_move in board.legal_moves:
            move_counter += 1
            if node is None:
                node = game.add_main_variation(next_move)
            else:
                node = node.add_main_variation(next_move)
            board.push(next_move)
            white_to_move = not white_to_move
    if board.is_checkmate():
        if debug:
            print("Black wins!" if white_to_move else "White wins!")
    else:
        if debug:
            print("It's a Draw!")
    print("%s moves total" % board.fullmove_number)
    print('\n\n')
    print(game)
    with open(join('game_results', f"{event}.pgn"), 'w') as f:
        f.write(str(game))
        f.write('\n')


def get_human_move(board):
    move = get_move_from_string(input("Enter a Valid Move: "), board)
    while not move:
        print("Invalid move. Try again.")
        move = get_move_from_string(input("Enter a Valid Move: "), board)
    return move

def get_move_from_string(istr, board):
    try:
        move = chess.Move.from_uci(istr)
        if move in board.legal_moves:
            return move
        else:
            return False
    except ValueError:
        return False


def play_one(fen=None):
    play_game(True, fen=fen)



def play_25():
    results = []
    for i in range(0, 25):
        results.append(play_game(False))
    print("%s White Wins" % len([a for a in results if a == "1-0"]))
    print("%s Black Wins" % len([a for a in results if a == "0-1"]))
    print("%s Draw" % len([a for a in results if a == "1/2-1/2"]))


if __name__ == '__main__':
    play_one()
