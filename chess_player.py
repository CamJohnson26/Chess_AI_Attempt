import chess
from chess_ai import ChessAi, evaluate_board_random, evaluate_board_simple_count

def play_game(debug):

    random_ai = ChessAi(evaluate_board_random)
    count_ai = ChessAi(evaluate_board_simple_count)
    board = chess.Board()
    white_to_move = True
    while not board.is_game_over():
        if debug:
            print("%s\n" % board)
        if white_to_move:
            next_move = random_ai.get_move(chess.WHITE, board)
        else:
            next_move = count_ai.get_move(chess.BLACK, board)
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
