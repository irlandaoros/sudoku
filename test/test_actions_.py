from test_github.board import create_new_board
from test_github.actions import place 

def test_place():
  board = create_new_board()
  place("X", [1, 1], board)
  assert board == [['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', '']]
  