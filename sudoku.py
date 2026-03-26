import math
import copy


# finding 0 or empty cells
def find_empty(board, size):
    for r in range(size):
        for c in range(size):
            if board[r][c] == 0:
                return r, c
    return None


# check if a number can be placed safely
def is_valid(board, num, pos, size):
    row, col = pos

    # checkinf row
    for c in range(size):
        if board[row][c] == num and c != col:
            return False

    # check column
    for r in range(size):
        if board[r][col] == num and r != row:
            return False

    #checking subgrid
    box_size = int(math.sqrt(size))
    box_row = row // box_size
    box_col = col // box_size

    for r in range(box_row * box_size, box_row * box_size + box_size):
        for c in range(box_col * box_size, box_col * box_size + box_size):
            if board[r][c] == num and (r, c) != pos:
                return False

    return True


# Checking if the initial board is valid or not 
def check_board(board, size):
    for r in range(size):
        for c in range(size):
            val = board[r][c]
            if val != 0:
                board[r][c] = 0
                if not is_valid(board, val, (r, c), size):
                    board[r][c] = val
                    return False
                board[r][c] = val
    return True


# backtracking
def solve(board, size):
    empty = find_empty(board, size)

    if not empty:
        return True

    row, col = empty

    for num in range(1, size + 1):
        if is_valid(board, num, (row, col), size):
            board[row][col] = num

            if solve(board, size):
                return True

            board[row][col] = 0    #undoing the changes if this doesn t work

    return False


# printing the boarD.
def print_board(board, size):
    box_size = int(math.sqrt(size))

    for i in range(size):
        if i % box_size == 0 and i != 0:
            print("-" * (size * 2 + box_size))

        for j in range(size):
            if j % box_size == 0 and j != 0:
                print("|", end=" ")

            val = board[i][j]
            print(val if val != 0 else "_", end=" ")

        print()


# taking input
def take_input(size):
    print(f"\nEnter your {size}x{size} Sudoku (use 0 for empty)\n")
    board = []

    for i in range(size):
        while True:
            row = input(f"Row {i+1}: ").split()

            if len(row) != size:
                print(f"Enter exactly {size} values")
                continue

            try:
                row = [int(x) for x in row]

                if all(0 <= num <= size for num in row):   #Checkiing
                    board.append(row)
                    break
                else:
                    print("Values out of range")
            except:
                print("Invalid input, try again")

    return board


print("Choose Sudoku size (perfect square only)")
size = int(input("Enter size (4 or 9 recommended): "))

if int(math.sqrt(size)) ** 2 != size:
    print("Size must be a perfect square (4, 9, 16...)")
    exit()

print("\n1. Use default puzzle")
print("2. Enter your own")

choice = input("Choice: ")

if choice == '1':
    if size == 9:
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],

            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],

            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    elif size == 4:
        board = [
            [1, 0, 0, 4],
            [0, 0, 3, 0],
            [0, 3, 0, 0],
            [2, 0, 0, 1]
        ]

    else:
        print("No default puzzle for this size")
        board = take_input(size)

else:
    board = take_input(size)


print("\nYou entered:\n")
print_board(board, size)


# creating a coPy so that the original board doesnt get messed up
board_copy = copy.deepcopy(board)

if not check_board(board_copy, size):
    print("\nInvalid puzzle (breaks Sudoku rules)")
elif solve(board_copy, size):
    print("\nSolved:\n")
    print_board(board_copy, size)
else:
    print("\nNo solution found (check input again)")