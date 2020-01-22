import chess

from chess import Piece

from src.Tablebase import Tablebase
from src.squares import square_map


class QueenVsRookPawn:

    @staticmethod
    def KQvKP(king_position: int):
        _BLACK_KING_POSITION = chess.H1
        _BLACK_PAWN_POSITION = chess.H2

        board = chess.Board()
        board.clear()

        board.set_piece_at(_BLACK_KING_POSITION, Piece(chess.KING, chess.BLACK))
        board.set_piece_at(_BLACK_PAWN_POSITION, Piece(chess.PAWN, chess.BLACK))
        board.set_piece_at(king_position, Piece(chess.KING, chess.WHITE))

        possible_boards = []

        for square in chess.SQUARES:
            if square in [_BLACK_KING_POSITION, _BLACK_PAWN_POSITION, king_position]:
                continue

            possible_board = board.copy()
            possible_board.set_piece_at(square, Piece(chess.QUEEN, chess.WHITE))

            if not possible_board.is_attacked_by(chess.WHITE, _BLACK_KING_POSITION) and possible_board.is_valid():
                possible_boards.append(possible_board)

        filtered_boards = list(filter(lambda b: Tablebase.check(b) == 2, possible_boards))

        return len(possible_boards) == len(filtered_boards)

    @staticmethod
    def KQvKP_test():
        for square in chess.SQUARES:
            print(square_map[square], "-->", QueenVsRookPawn.KQvKP(square))
