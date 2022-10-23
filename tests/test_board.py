from .. import board


def test_board():
    test_board = board.Board()
    assert test_board.diameter == 5
