class Board:
    EDGE = 3
    WIN_REACH = 3
    PIECE = (" ", "o", "x")
    MARU = 1
    BATSU = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(EDGE)]
    AXIS = [i for i in range(10)]


    def __init__(self):
        self.grid_data = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        self.piece = -1


    def input_(self):
        while True:
            self.show()
            print("\nYou :", self.PIECE[self.piece], "\n1 ~", self.EDGE, "で入力してください。")
            x, y = input("X = "), input("Y = ")
            if x in self.ALLOWED_NUMBERS and y in self.ALLOWED_NUMBERS:
                x, y = int(x)-1, int(y)-1
                if self.grid_data[y][x] != self.EMPTY:
                    print("そのマスは空いていません。")
                else:
                    return x, y
            else:
                print("1 ~", self.EDGE, "で入力してください。")


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
                print(self.PIECE[self.grid_data[i][j]], end = " ")
            print()

    
    def grid_check(self, i, j):
        if self.grid_data[i][j] == self.piece:
            return True


    def arround_check(self, i, j, n, m):
        if (n != 0 or m != 0) and (0 <= i+n <= self.EDGE-1 and 0 <= j+m <= self.EDGE-1):
            if self.grid_data[i+n][j+m] == self.piece:
                return True


    def count(self, i, j, n, m):
        count = 1
        for t in range(self.EDGE):
            if 0 <= i+n*(t+1) <= self.EDGE-1 and 0 <= j+m*(t+1) <= self.EDGE-1:
                if self.grid_data[i+n*(t+1)][j+m*(t+1)] == self.piece:
                    count += 1
                    if count == self.WIN_REACH:
                        self.show()
                        print("\n" + self.PIECE[self.piece], "WIN")
                        return True
        if turn == self.EDGE**2:
            self.show()
            print("\nDRAW")
            return True


    def trial(self):
        for i in range(self.EDGE):
            for j in range(self.EDGE):
                if self.grid_check(i, j):
                    for n in (-1, 0, 1):
                        for m in (-1, 0, 1):
                            if self.arround_check(i, j, n, m):
                                if self.count(i, j, n, m):
                                    return True


board = Board()
turn = 0
while True:
    board.piece *= -1
    turn += 1
    x, y = board.input_()
    board.set_(x, y)
    if board.trial():
        break