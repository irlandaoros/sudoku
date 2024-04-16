from actions import add_number_to_cell 
from board import print_board 
from actions import erase_number
from actions import color_number 
from board import erase 
from board import print_new_board 

with open('README.md', 'r') as f:
   print (f.read())
  
while True:
  command = input("Enter a command: ")
  if command == "add number to cell":
    number=None 
    position=None
    grid=None
    add_number_to_cell (number,position,grid)
  elif command == "change number":
    number=None
    position=None
    grid=None
    change_number (number,position,grid)
  elif command == "erase number":
    eraser=None
    number=None
    position=None
    grid=None 
    erase_number (eraser,number,position,grid)
  elif command == "color number":
    color=None
    position=None
    color_number (color,position)
  elif command == "if win":
    change_board=None 
  else:
    print("I did not understand that command")
  
  
 
