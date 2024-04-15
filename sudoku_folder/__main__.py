with open('README.md', 'r') as f:
  print (f.read())
  
while True:
  command = input("Enter a command: ")
  if command == "add number to cell":
    number=None 
    position=None
    grid=None
    add_number_to_cell (number,position,grid)
  
  
 
