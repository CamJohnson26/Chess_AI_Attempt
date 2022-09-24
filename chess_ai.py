import chess
from random import randint, shuffle


class ChessAi:

    def __init__(self, eval_function, depth):
        self.eval_function = eval_function
        self. depth = depth
        pass

    def get_move(self, board):
        move = self.get_strongest_move(board)
        return move

    # Worth noting: It looks depth_limit moves deep after the current player moves once, so limit of 3 looks 4 moves ahead
    # Had some issues getting intuition about what the returned score represents
    # It's always scoring your opponent, so the result will be your opponents best possible outcome
    def minimax(self, depth_limit, cur_depth, board, alpha=-9999, beta=9999, is_max_player=True):
        if cur_depth == 0:
            a = self.eval_function(board) * (-1 if board.turn else 1) * (-1 if is_max_player else 1)
            if a == 9999:
                a = a - depth_limit # prefer an earlier checkmate
            if a == -9999:
                a = a + depth_limit
            return a
        moves = board.legal_moves
        if moves.count() == 0:
            if board.is_checkmate():
                score = 9999
                mate_move_adjusted = -1 * (depth_limit - cur_depth)
                score = (score + mate_move_adjusted) * (-1 if is_max_player else 1)
                return score
            return 0
        if is_max_player:
            best_score = -9999 # Assume the other player's best move is horrible for them
            a = alpha
            for move in moves:
                board.push(move)
                best_score = max(best_score, self.minimax(depth_limit, cur_depth - 1, board, alpha=a, beta=beta, is_max_player=not is_max_player))
                board.pop()
                a = max(a, best_score)
                if beta <= a:
                    break
            mate_move_adjusted = depth_limit - cur_depth if best_score == -9999 else 0
            return best_score + mate_move_adjusted
        else:
            best_score = 9999 # Assume that the other player's best move is perfect for them
            b = beta
            for move in moves: # We'll pick whichever move gives them the lowest score
                board.push(move)
                best_score = min(best_score, self.minimax(depth_limit, cur_depth - 1, board, alpha=alpha, beta=b, is_max_player=not is_max_player))
                board.pop()
                b = min(b, best_score)
                if b <= alpha:
                    break
            mate_move_adjusted = -1 * (depth_limit - cur_depth) if best_score == 9999 else 0
            return best_score + mate_move_adjusted

    def get_strongest_move(self, board):
        sorted_moves = self.rank_moves(board)
        return [a[1] for a in sorted_moves][0]

    def rank_moves(self, board):
        score_sign = -1 if board.turn else 1
        moves = list(board.legal_moves)
        shuffle(moves)
        ranked_moves = []
        for move in moves:
            board.push(move)
            score = self.minimax(self.depth, self.depth, board) * score_sign
            ranked_moves.append((score, move))
            board.pop()
        sorted_moves = sorted(ranked_moves, key=lambda i: i[0], reverse=score_sign == -1)
        return sorted_moves


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
    if board.is_checkmate():
        return -9999 if board.turn == chess.WHITE else 9999
    if board.is_stalemate() or board.is_insufficient_material(): # or board.can_claim_draw(): Very slow check
        return 0
    return score
