import chess
from chess_ai import ChessAi

def play_game():

    ai = ChessAi()
    board = chess.Board()
    white_to_move = True

    while not board.is_game_over():
        print("%s\n" % board)
        if white_to_move:
            next_move = ai.get_move(board)
        else:
            next_move = ai.get_move(board)
        if next_move in board.legal_moves:
            board.push(next_move)
            white_to_move = not white_to_move
    if board.is_checkmate():
        print("Black wins!" if white_to_move else "White wins!")
    else:
        print("It's a Draw!")


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

if __name__ == '__main__':
    play_game()