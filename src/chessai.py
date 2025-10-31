import random

import chess

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 90,
}

class ChessAI:
    def __init__(self, colour = chess.WHITE, debug = False):
        self.debug = debug
        self.colour = colour
        self.search_depth = 4
        self.alpha = -float('inf')
        self.beta = float('inf')

    def evaluate_position(self, board):
        score = 0
        for piece_type in PIECE_VALUES:
            score += len(board.pieces(piece_type, self.colour)) * PIECE_VALUES[piece_type]
            score -= len(board.pieces(piece_type, not self.colour)) * PIECE_VALUES[piece_type]
        if self.colour == chess.BLACK:
            score = -score
        return score


    def move(self, board) -> chess.Move:
        best_move = random.choice(list(board.legal_moves))
        best_value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            board_value = self._minimax(board, self.search_depth, self.alpha, self.beta, False)
            board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
        if self.debug:
            print(f"Chosen move: {best_move}, Value: {best_value}")
        return best_move
    
    def _minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return self.evaluate_position(board)

        if maximizing:
            max_eval = -float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self._minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self._minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval