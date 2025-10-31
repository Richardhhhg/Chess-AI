import random
import time

import chess

from chessai import ChessAI

board = chess.Board()
bot = ChessAI(debug = True)

while not board.is_game_over():
    move = bot.move(board)
    board.push(move)
    player_move = input("Black's Move (in UCI format): ")
    board.push(chess.Move.from_uci(player_move))
    print(board)