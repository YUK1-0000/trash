class Board:
    EDGE = 8
    WIN_REACH = 4
    PIECE = ("", "o", "x")
    MARU = 1
    BATSU = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(EDGE)]
    AXIS = ("0", "1", "2", "3", "4", "5", "6" ,"7", "8", "9")
    def __init__(self):
        self.grid_data = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        self.piece = -1

    def input_(self):
        while True:
            x = input("X = ")
            y = input("Y = ")
            if x in board.ALLOWED_NUMBERS and y in board.ALLOWED_NUMBERS:
                x, y = int(x)-1, int(y)-1
                if board.grid_data[y][x] != board.EMPTY:
                    print("そのマスは空いていません。")
                else:
                    break
            else:
                print("1 ~", board.EDGE, "で入力してください。")

    def set_(self, x, y):
        self.grid_data[y][x] = self.piece
        
    def show(self):
        self.grid = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        for i in range(self.EDGE+1):
            print(self.AXIS[i], end = " ")
        print()
        for i in range(self.EDGE):
            print(self.AXIS[i+1], end = " ")
            for j in range(self.EDGE):
                if self.grid_data[i][j] == self.BATSU:
                    print("x", end = " ")
                elif self.grid_data[i][j] == self.MARU:
                    print("o", end = " ")
                else:
                    print(" ", end = " ")      
            print()

    def trial(self):
        BREAK = False
        for i in range(board.EDGE):
            for j in range(board.EDGE):
                if board.grid_data[i][j] == board.piece:
                    for n in (-1, 0, 1):
                        for m in (-1, 0, 1):
                            if (n != 0 or m != 0) and (0 <= i+n <= board.EDGE-1 and 0 <= j+m <= board.EDGE-1):
                                if board.grid_data[i+n][j+m] == board.piece:
                                    count = 1
                                    for t in range(board.EDGE):
                                        if 0 <= i+n*(t+1) <= board.EDGE-1 and 0 <= j+m*(t+1) <= board.EDGE-1:
                                            if board.grid_data[i+n*(t+1)][j+m*(t+1)] == board.piece:
                                                count += 1
                                                if BREAK:
                                                    break
                                                elif count == board.WIN_REACH:
                                                    board.show()
                                                    print("\n" + board.PIECE[board.piece], "WIN")
                                                    BREAK = True
                                                    return True
                                                elif turn == board.EDGE**2:
                                                    board.show()
                                                    print("\nDRAW")
                                                    BREAK = True
                                                    return True



board = Board()
turn = 0
while not board.trial():
    board.piece *= -1
    turn += 1

    while True:
        board.show()
        print("\nYou :", board.PIECE[board.piece])
        x = input("\nX = ")
        y = input("Y = ")
        if x in board.ALLOWED_NUMBERS and y in board.ALLOWED_NUMBERS:
            x, y = int(x)-1, int(y)-1
            if board.grid_data[y][x] != board.EMPTY:
                print("そのマスは空いていません。")
            else:
                break
        else:
            print("1 ~", board.EDGE, "で入力してください。")

    board.set_(x, y)
    board.trial()