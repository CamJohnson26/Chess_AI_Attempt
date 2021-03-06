import chess
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def play_game(debug):

    random_ai = ChessAi(evaluate_board_random, 0)
    count_ai_1 = ChessAi(evaluate_board_simple_count, 1)
    count_ai_2 = ChessAi(evaluate_board_simple_count, 2)
    count_ai_3 = ChessAi(evaluate_board_simple_count, 3)
    count_ai_4 = ChessAi(evaluate_board_simple_count, 4)
    count_ai_5 = ChessAi(evaluate_board_simple_count, 5)
    count_ai_6 = ChessAi(evaluate_board_simple_count, 6)
    board = chess.Board()
    white_to_move = True
    while not board.is_game_over():
        if debug:
            print(white_to_move)
            print("%s\n" % board)
        if white_to_move:
            next_move = count_ai_2.get_move(chess.WHITE, board)
        else:
            next_move = count_ai_4.get_move(chess.BLACK, board)
        if next_move in board.legal_moves:
            board.push(next_move)
            white_to_move = not white_to_move
    if board.is_checkmate():
        if debug:
            print("Black wins!" if white_to_move else "White wins!")
    else:
        if debug:
            print("It's a Draw!")
    print("%s moves total" % board.fullmove_number)
    return board.result()


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


def play_one():
    play_game(True)



def play_25():
    results = []
    for i in range(0, 25):
        results.append(play_game(False))
    print("%s White Wins" % len([a for a in results if a == "1-0"]))
    print("%s Black Wins" % len([a for a in results if a == "0-1"]))
    print("%s Draw" % len([a for a in results if a == "1/2-1/2"]))


if __name__ == '__main__':
    print(play_one())
