import chess
from random import randint, shuffle


class ChessAi:

    def __init__(self, eval_function):
        self.eval_function = eval_function
        pass

    def get_move(self, player, board):
        move = self.get_strongest_move(player, board)
        return move

    def minimax(self, depth, is_max_player, board):
        if depth == 0:
            return self.eval_function(board) * (1 if is_max_player else -1)
        if is_max_player:
            best_score = -9999
            for move in board.legal_moves:
                board.push(move)
                best_score = max(best_score, self.minimax(depth - 1, not is_max_player, board))
                board.pop()
            return best_score
        else:
            best_score = 9999
            for move in board.legal_moves:
                board.push(move)
                best_score = min(best_score, self.minimax(depth - 1, not is_max_player, board))
                board.pop()
            return best_score

    def get_strongest_move(self, player, board):
        moves = list(board.legal_moves)
        ranked_moves = []
        for move in moves:
            board.push(move)
            score = self.minimax(4, True, board)
            ranked_moves.append((score, move))
            board.pop()
        sorted_moves = sorted(ranked_moves, key=lambda i: i[0], reverse=True)
        return [a[1] for a in sorted_moves][0]


def evaluate_board_random(board):
    return randint(-5, 5)


def evaluate_board_simple_count(board):
    return sum([
        len(board.pieces(chess.PAWN, chess.WHITE)) * 1,
        len(board.pieces(chess.PAWN, chess.BLACK)) * -1,
        len(board.pieces(chess.KNIGHT, chess.WHITE)) * 3,
        len(board.pieces(chess.KNIGHT, chess.BLACK)) * -3,
        len(board.pieces(chess.BISHOP, chess.WHITE)) * 3,
        len(board.pieces(chess.BISHOP, chess.BLACK)) * -3,
        len(board.pieces(chess.ROOK, chess.WHITE)) * 5,
        len(board.pieces(chess.ROOK, chess.BLACK)) * -5,
        len(board.pieces(chess.QUEEN, chess.WHITE)) * 9,
        len(board.pieces(chess.QUEEN, chess.BLACK)) * -9,
        len(board.pieces(chess.KING, chess.WHITE)) * 9000,
        len(board.pieces(chess.KING, chess.BLACK)) * -9000
    ])

