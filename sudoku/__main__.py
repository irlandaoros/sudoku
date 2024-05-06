from actions import add_number_to_cell 
from board import print_board 
from actions import erase_number
from board import erase
from board import create_new_board
from actions import change_number

with open('README.md', 'r') as f:
   print (f.read())
   
# Game starts:
grid = create_new_board()
while True:
  # Once per turn:
  print_board(grid)
  command = input("Enter a command: ")
  if command == "add number to cell":
    # When command is used:
    number=input("Enter a number")
    position=input("Enter a position")
    add_number_to_cell (number,position,grid)
  elif command == "change number":
    number=None
    position=None
    change_number (number,position,grid)
  elif command == "erase number":
    eraser=None
    number=None
    position=None
    erase_number (eraser,number,position,grid)
  elif command == "color number":
    color=None
    position=None
    color_number (color,position)
  elif command == "if win":
    change_board=None 
  else:
    print("I did not understand that command")
  
  