'''
HW for week1
'''

'''
Homework 1: Understanding Tetris Block Rotation
'''

# Here is a 'T' shaped Tetris block represented as a 2D array
# 1 represents a filled cell, 0 represents an empty cell
t_block = [
    [0, 1, 0],
    [1, 1, 1]
]

# What happens when we rotate this block 90 degrees clockwise?
# Fill in the rotated block below
rotated_t_block = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0]
]

# Let's print both blocks to check
print("Original T Block:")
for row in t_block:
    for cell in row:
        if cell == 1:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

print("\nRotated T Block:")
for row in rotated_t_block:
    for cell in row:
        if cell == 1:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

# Additional Challenge:
# 1. Create an 'L' shaped block and rotate it 90 degrees
l_block = [
    [1, 0],
    [1, 0],
    [1, 1]
]
rotated_l_block = [
    [1, 1, 1],
    [1, 0, 0]
]

# 2. Create a 'Z' shaped block and rotate it 90 degrees
z_block = [
    [1, 1, 1],
    [0, 1, 1]
]
rotated_z_block = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

# Hint: Draw the shapes on paper first and observe how they change when rotated!

'''
Homework 2: Understanding Collision Detection
'''

# This is a small Tetris game board (6x6)
# 0 represents an empty space, 1 represents a filled space (with blocks)
board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0]
]

# Here is a 'T' shaped block
t_block = [
    [0, 1, 0],
    [1, 1, 1]
]


# Function to print the board
def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print("□", end=" ")
            else:
                print("■", end=" ")
        print()


# Function to check for collisions
def check_collision(board, block, block_x, block_y):
    """
    board: the game board
    block: the block to check
    block_x, block_y: top-left coordinates of the block

    Returns: True if there's a collision, False otherwise
    """
    for y in range(len(block)):
        for x in range(len(block[0])):
            if block[y][x] == 1:
                # Check if out of bounds
                if (y + block_y < 0 or
                        x + block_x < 0 or
                        y + block_y >= len(board) or
                        x + block_x >= len(board[0])):
                    return True
                # Check if colliding with another block
                if board[y + block_y][x + block_x] == 1:
                    return True
    return False


# Function to place a block on the board
def place_block(board, block, block_x, block_y):
    """Places the block on the board. Does not check for collisions."""
    new_board = [row[:] for row in board]  # Copy the board

    for y in range(len(block)):
        for x in range(len(block[0])):
            if block[y][x] == 1:
                new_board[y + block_y][x + block_x] = 1

    return new_board


# Print the original board
print("Original Game Board:")
print_board(board)
print()

# Task 1: Check if the T block can be placed at position (2, 1), and if possible, print the result
# Hint: Use the check_collision function to verify, and the place_block function to place it

position_x = 2
position_y = 1

# Write your code here
# Check for collision and print the result


# Task 2: Experiment with placing the T block at different positions
# Check if the following positions are valid and print the results:
test_positions = [(0, 0), (3, 3), (2, 4), (0, 4)]

# Write your code here
# Check each position for collisions and print the results


# Task 3: Rotate and place a block
# Use the rotated_t_block from the previous homework (or define it again here)
# Experiment to see if the rotated block can be placed in positions where the original block cannot

# Write your code here
# Define the rotated block and attempt to place it at various positions