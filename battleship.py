from random import randint

board = []
ships = []
battleship = 4
cruiser = 3
pt_boat = 2
aircraft_carrier = 5

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

def place_ship(ship,ships):
    orientation = randint(0,1)
    if (orientation == 0):
        ship_row = randint(0, len(board) - 1 - ship)
        ship_col = randint(0, len(board) - 1)
    else:
        ship_row = randint(0, len(board) - 1)
        ship_col = randint(0, len(board) - 1 - ship)
        
    ship_spot = []
    for i in range(0,ship):
        if orientation == 0:
            ship_spot.append([ship_row + i, ship_col])
        else:
            ship_spot.append([ship_row, ship_col + i])
    # Make sure there are no conflicts
    redo = False
    for ship in ships:
        for coord in ship:
            for spots in ship_spot:
                if coord[0] == spots[0] and coord[1] == spots[1]:
                    redo = True
    if redo:
        place_ship(ship)
    else:
        ships.append(ship_spot)
        return ship_spot

def grab_guess(board):
    while True:
        guess_row = int(raw_input("Guess Row (0-9):"))
        guess_col = int(raw_input("Guess Col (0-9):"))
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print "Please keep your guess on the board!"
        else:
            if board[guess_row][guess_col] != "O":
                print "You have already fired at that coordinate!"
            else:
                break
    return [guess_row,guess_col]

place_ship(aircraft_carrier,ships)
place_ship(battleship,ships)
place_ship(cruiser,ships)
place_ship(pt_boat,ships)

# Number of misses to allow
misses = 20
num_hits = 0
max_hits = 0
for ship in ships:
    for coord in ship:
        max_hits += 1
while misses > 0:
    print "Misses remaining: %s" % misses
    print_board(board)
    print
    guess = grab_guess(board)
    hit = False
    for ship in ships:
        for coord in ship:
            if guess[0] == coord[0] and guess[1] == coord[1]:
                hit = True
                num_hits += 1
                break
        if hit:
            break
    guess_row = guess[0]
    guess_col = guess[1]
    if hit:
        print "HIT!"
        # mark the board
        board[guess_row][guess_col] = "H"
        # is the game over?
        if num_hits >= max_hits:
            print "Congratulations! You sank all of the ships!"
            break
    else:
        # mark the board
        print "MISS!"
        board[guess_row][guess_col] = "X"
        misses -= 1
# Add S's to the board for where the ships were hidden but weren't hit
for ship in ships:
    for coord in ship:
        ship_row = coord[0]
        ship_col = coord[1]
        if board[ship_row][ship_col] == "O":
            board[ship_row][ship_col] = "S"
print_board(board)
print "Game Over"
