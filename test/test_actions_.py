from sudoku.board import create_new_board
from sudoku.actions import add_number_to_cell, change_number, erase_number, if_win

def test_add_number_to_cell():
  board = create_new_board()
  add_number_to_cell("1", [1, 1], board)
  assert board == [['', '', '', '', '', '', '', '', ''],
                   ['', '1', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', '']]
  
def test_change_number():
  board = create_new_board()
  add_number_to_cell("1", [1, 1], board)
  change_number("2", [1,1], board)
  assert board == [['', '', '', '', '', '', '', '', ''],
                   ['', '2', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', ''],
                   ['', '', '', '', '', '', '', '', '']]
  

  def test_erase_number():
    board = create_new_board()
    add_number_to_cell("1", [1, 1], board)
    erase_number("", [1,1], board)
    assert board == [['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '']]
    
def test_if_win():

  board = create_new_board()
  add_number_to_cell("1", [1, 1], board)
  result = if_win ()
  assert result == False
