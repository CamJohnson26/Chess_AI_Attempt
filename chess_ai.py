import chess
from random import randint, shuffle


class ChessAi:

    def __init__(self, eval_function, depth):
        self.eval_function = eval_function
        self. depth = depth
        pass

    def get_move(self, player, board):
        move = self.get_strongest_move(player, board)
        return move

    def minimax(self, depth, is_white, board, alpha=-9999, beta=9999, is_max_player=True):
        if depth == 0:
            a = self.eval_function(board) * (-1 if is_white else 1)
            return a
        moves = board.legal_moves
        if is_max_player:
            best_score = -9999
            a = alpha
            for move in moves:
                board.push(move)
                best_score = max(best_score, self.minimax(depth - 1, is_white, board, alpha=a, beta=beta, is_max_player=not is_max_player))
                board.pop()
                a = max(a, best_score)
                if beta <= a:
                    break
            return best_score
        else:
            best_score = 9999
            b = beta
            for move in moves:
                board.push(move)
                best_score = min(best_score, self.minimax(depth - 1, is_white, board, alpha=alpha, beta=b, is_max_player=not is_max_player))
                board.pop()
                b = min(b, best_score)
                if b <= alpha:
                    break
            return best_score

    def get_strongest_move(self, player, board):
        moves = list(board.legal_moves)
        shuffle(moves)
        ranked_moves = []
        for move in moves:
            board.push(move)
            score = self.minimax(self.depth, not board.turn, board)
            ranked_moves.append((score, move))
            board.pop()
        sorted_moves = sorted(ranked_moves, key=lambda i: i[0])
        print(sorted_moves)
        return [a[1] for a in sorted_moves][0]


def evaluate_board_random(board):
    return randint(-5, 5)


def evaluate_board_simple_count(board):
    score = (
        len(board.pieces(chess.PAWN, chess.WHITE)) * 1 +
        len(board.pieces(chess.PAWN, chess.BLACK)) * -1 +
        len(board.pieces(chess.KNIGHT, chess.WHITE)) * 3 +
        len(board.pieces(chess.KNIGHT, chess.BLACK)) * -3 +
        len(board.pieces(chess.BISHOP, chess.WHITE)) * 3 +
        len(board.pieces(chess.BISHOP, chess.BLACK)) * -3 +
        len(board.pieces(chess.ROOK, chess.WHITE)) * 5 +
        len(board.pieces(chess.ROOK, chess.BLACK)) * -5 +
        len(board.pieces(chess.QUEEN, chess.WHITE)) * 9 +
        len(board.pieces(chess.QUEEN, chess.BLACK)) * -9 +
        len(board.pieces(chess.KING, chess.WHITE)) * 9000 +
        len(board.pieces(chess.KING, chess.BLACK)) * -9000
    )
    if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw():
        return 0
    return score
