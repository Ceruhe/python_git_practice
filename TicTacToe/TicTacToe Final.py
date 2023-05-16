import random

# potential improvements:
# let player select to go first/second (current default > player goes first, player is X)
# choose symbol (currently not flexible)
# option to disable computer to play against another person
# logic for computer (check Solved Game; sum line/columns?)
# option to quick restart game, game counter

player = "X"
COUNT = 9
VALID_RANGE = range(1, 10)

GRID = [{7: "7", 8: "8", 9: "9"},
        {4: "4", 5: "5", 6: "6"},
        {1: "1", 2: "2", 3: "3"},
        {7: "7", 4: "4", 1: "1"},
        {8: "8", 5: "5", 2: "2"},
        {9: "9", 6: "6", 3: "3"},
        {1: "1", 5: "5", 9: "9"},
        {3: "3", 5: "5", 7: "7"}]


# shows the current moves in the grid
def display_grid():

    print("-" * 19)
    print(f'|  {GRID[0][7]}  |  {GRID[0][8]}  |  {GRID[0][9]}  |')
    print("-" * 19)
    print(f'|  {GRID[1][4]}  |  {GRID[1][5]}  |  {GRID[1][6]}  |')
    print("-" * 19)
    print(f'|  {GRID[2][1]}  |  {GRID[2][2]}  |  {GRID[2][3]}  |')
    print("-" * 19)
    print()


# gets the move of the current player and sends it get validated before returning
def select_move(current_player, grid):

    move = None

    while move not in VALID_RANGE:

        display_grid()

        try:
            if current_player == "X":
                move = int(input("Pick your number: "))
                current_player, move = move_validation(current_player, move, grid)

                while move is False:
                    move = int(input("Square was already picked, choose another one!" ))

            else:
                move = random.randint(1, 9)
                #move = int(input("test: "))
                current_player, move = move_validation(current_player, move, grid)
                print("Computer's move was:", move)

        except ValueError:
            print("Looking for a valid number!")

    return update_grid(current_player, move, grid)


# checks if the move has not already been made by either player
def move_validation(current_player, move, grid):

    previous_player = swap_player(current_player)

    for line in grid:                   # runs through each index(dictionary) in grid, 8 in total
        for key_digit in line:          # looks through each dictionary
            if key_digit == move:       # checks if a key is the same digit as move
                # checks if they key has the value of either player
                if line.get(move) == current_player or line.get(move) == previous_player:
                    move = False        # sets the move to False to stay in the loop once returning
                    continue

                else:
                    return current_player, move

    return current_player, move


# updates the grid with a valid move by the current player
def update_grid(current_player, move, grid):

    for line in grid:
        if move in line:
            line[move] = current_player

    return check_winner(current_player, grid)


# checks for winner/tie
def check_winner(current_player, updated_grid):

    # sets winning conditions to the current player for the current grid to check against to determine winner
    winning_conditions = [{7: current_player, 8: current_player, 9: current_player},
                          {4: current_player, 5: current_player, 6: current_player},
                          {1: current_player, 2: current_player, 3: current_player},
                          {7: current_player, 4: current_player, 1: current_player},
                          {8: current_player, 5: current_player, 2: current_player},
                          {9: current_player, 6: current_player, 3: current_player},
                          {1: current_player, 5: current_player, 9: current_player},
                          {3: current_player, 5: current_player, 7: current_player}]

    for grid_line in updated_grid:      # goes through every index(dictionary) in the grid and winning conditions
        for winning_line in winning_conditions:
            if grid_line.keys() == winning_line.keys():  # compares keys in both arrays
                if grid_line == winning_line in winning_conditions:  # matches key/values for each line in both arrays
                    display_grid()
                    print("Winner winner chicken dinner!")
                    quit()

    if COUNT == 0:
        display_grid()
        print("This match results in a tie.")
        quit()

    else:
        counter()
        current_player = swap_player(current_player)
        return select_move(current_player, updated_grid)


def swap_player(previous_player):
    current_player = previous_player

    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"

    return current_player


# counts how many moves have been made; used to end the game once there are no available moves left
def counter():
    global COUNT
    COUNT -= 1
    return


select_move(player, GRID)


