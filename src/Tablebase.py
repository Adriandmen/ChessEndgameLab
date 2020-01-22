import chess.syzygy

from chess import Board


class Tablebase:

    TABLEBASE_PATH = "C:\\D\\chess\\tablebase.sesse.net\\syzygy\\3-4-5"
    TABLEBASE = chess.syzygy.open_tablebase(TABLEBASE_PATH)

    @staticmethod
    def check(board: Board):
        return Tablebase.TABLEBASE.probe_wdl(board)


