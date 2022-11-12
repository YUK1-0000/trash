turn = 0
white_piece = 0
black_piece = 0

AXIS_NUMBERS = ("０", "１", "２", "３", "４", "５", "６" ,"７", "８")
ALLOWED_NUMBERS = tuple(map(lambda i: str(i+1), range(8)))


grid = [["＋" for _ in range(8)] for _ in range(8)]
grid[3][3] = "○"
grid[3][4] = "●"
grid[4][3] = "●"
grid[4][4] = "○"

def PRINT_X():
    print("０１２３４５６７８")

def PRINT_Y_GRID():
    for i in range(8):
        print(AXIS_NUMBERS[i+1],"".join(grid[i]), sep = "")



PRINT_X()
PRINT_Y_GRID()


while turn < 60 and any("○" in grid[i] for i in range(8)) and any("●" in grid[i] for i in range(8)):

    turn += 1
    X = 4
    Y = 4

    if turn % 2 == 0:
        piece = "●"
    else:
        piece = "○"
    print("\nYou :", piece)

    while True:
        while True:
            X = input("X = ")
            Y = input("Y = ")
            if X in ALLOWED_NUMBERS and Y in ALLOWED_NUMBERS:
                X, Y = int(X)-1, int(Y)-1
                break
            else:
                print("Error!")
        if grid[Y][X] == "＋":
            break
        else:
            print("Error!")
  

    grid_count = 0
    for i in range(Y):
        print("i    ", i)
        if grid[Y-i-1][X] == piece or grid[Y-i-1][X] == "＋":
            print("Y1", Y-i-1)
            break
        else:
            grid_count += 1
            print("grid count1", grid_count)
    if grid_count > 0:
        print("grid count2", grid_count)
        for j in range(grid_count):
            print(range(grid_count))
            print("Y2", Y-j-1)
            grid[Y-j-1][X] = piece


    grid[Y][X] = piece
    PRINT_X()
    PRINT_Y_GRID()