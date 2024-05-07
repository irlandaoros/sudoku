def add_number_to_cell(number, position, grid):
    # According to the example of Samantha García (2024)
    print("Add number to cell")
    try:
        row_n, col_n = int(position[0]), int(position[2])
        row_n -= 1  # Adjusting to 0-based index
        col_n -= 1
        if 0 <= row_n < 9 and 0 <= col_n < 9:  # Check if position is valid
            grid[row_n][col_n] = number
            print("Number added successfully!")
        else:
            print("Invalid position. Please enter a position within the range 1-9 for both row and column.")
    except ValueError:
        print("Invalid position format. Please enter the position as two integers separated by a comma.")

def change_number(number, position, grid):
    print("Change number")
    try:
        row_n, col_n = position
        row_n -= 1  # Adjusting to 0-based index
        col_n -= 1
        if 0 <= row_n < 9 and 0 <= col_n < 9:  # Check if position is valid
            if grid[row_n][col_n] != 0:  # Check if cell is not empty
                grid[row_n][col_n] = number
                print("Number changed successfully!")
            else:
                print("Cell is empty. Nothing to change.")
        else:
            print("Invalid position. Please enter a position within the range 1-9 for both row and column.")
    except ValueError:
        print("Invalid position format. Please enter the position as two integers separated by a comma.")

def erase_number(position, grid):
    print("Erase number")
    try:
        row_n, col_n = position
        row_n -= 1  # Adjusting to 0-based index
        col_n -= 1
        if 0 <= row_n < 9 and 0 <= col_n < 9:  # Check if position is valid
            if grid[row_n][col_n] != 0:  # Check if cell is not empty
                grid[row_n][col_n] = 0
                print("Number erased successfully!")
            else:
                print("Cell is already empty.")
        else:
            print("Invalid position. Please enter a position within the range 1-9 for both row and column.")
    except ValueError:
        print("Invalid position format. Please enter the position as two integers separated by a comma.")

def if_win(grid):
    print("Check if win")
    for row in grid:
        if 0 in row:  # If any cell contains 0, the game is not yet won
            return False
    print("Congratulations! You've won the game!")
    return True
