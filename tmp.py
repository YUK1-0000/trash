class Board:
    EDGE = 3
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
            X = input("X = ")
            Y = input("Y = ")
            if X in board.ALLOWED_NUMBERS and Y in board.ALLOWED_NUMBERS:
                X, Y = int(X)-1, int(Y)-1
                if board.grid_data[Y][X] != board.EMPTY:
                    print("そのマスは空いていません。")
                else:
                    break
            else:
                print("1 ~", board.EDGE, "で入力してください。")   

    def set_(self, X, Y):
        self.grid_data[Y][X] = self.piece
        
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
        for i in range(self.EDGE):
            for j in range(self.EDGE):
                if self.grid_data[i][j] == self.piece:
                    for n in (-1, 0, 1):
                        for m in (-1, 0, 1):
                            if (n != 0 or m != 0) and (0 <= i+n <= self.EDGE-1 and 0 <= j+m <= self.EDGE-1):
                                if self.grid_data[i+n][j+m] == self.piece:
                                    count = 1
                                    for t in range(self.EDGE):
                                        if 0 <= i+n*(t+1) <= self.EDGE-1 and 0 <= j+m*(t+1) <= self.EDGE-1:
                                            if self.grid_data[i+n*(t+1)][j+m*(t+1)] == self.piece:
                                                count += 1
                                                if BREAK:
                                                    break
                                                elif count == self.EDGE:
                                                    self.show()
                                                    print("\n", self.PIECE[self.piece], "WIN")
                                                    BREAK = True
                                                elif turn == self.EDGE**2:
                                                    self.show()
                                                    print("\nDRAW")
                                                    BREAK = True




board = Board()
turn = 0
while BREAK == False:
    board.show()
    board.piece *= -1
    turn += 1
    print("\nYou :", board.PIECE[board.piece])

    while True:
        X = input("X = ")
        Y = input("Y = ")
        if X in board.ALLOWED_NUMBERS and Y in board.ALLOWED_NUMBERS:
            X, Y = int(X)-1, int(Y)-1
            if board.grid_data[Y][X] != board.EMPTY:
                print("そのマスは空いていません。")
            else:
                break
        else:
            print("1 ~", board.EDGE, "で入力してください。")

    board.set_(X, Y)
    board.trial()