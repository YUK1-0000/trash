class Board:
    EDGE = 8
    WIN_REACH = 3
    PIECE = (" ", "○", "●")
    WHITE = 1
    BLACK = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(EDGE)]
    AXIS = [i for i in range(10)]


    def __init__(self):
        self.grid_data = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        for y in (3, 4):
            for x in (3, 4):
                if y == x:
                    self.grid_data[y][x] = self.WHITE
                else:
                    self.grid_data[y][x] = self.BLACK
        self.piece = -1

            
    def show(self):
        print()
        self.grid = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        for i in range(self.EDGE+1):
            print(self.AXIS[i], end = " ")
        print()
        for i in range(self.EDGE):
            print(self.AXIS[i+1], end = " ")
            for j in range(self.EDGE):
                print(self.PIECE[self.grid_data[i][j]], end = " ")
            print()
            

    def set_(self, x, y):
        self.grid_data[y][x] = self.piece


    def trun(self, x, y):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if 0 <= y+i < self.EDGE and 0 <= x+j < self.EDGE:
                    if self.grid_data[y+i][x+j] == self.piece*-1:
                        # print(f"o  y {1+y+i}  x {1+x+j}")
                        count = 1
                        for n in range(self.EDGE):
                            if 0 <= y+i*(n+1) < self.EDGE and 0 <= x+j*(n+1) < self.EDGE:
                                if self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece*-1:
                                    count += 1
                                    # print(f"1  y {1+y+i*(n+1)}  x {1+x+j*(n+1)}")
                                elif self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece:
                                    for m in range(count):
                                        # print(f"2  y {1+y+i*(m+1)}  x {1+x+j*(m+1)}")
                                        self.grid_data[y+i*(m+1)][x+j*(m+1)] = self.piece

                                    
    def piece_count(self):
        white_count = 0
        black_count = 0
        for i in range(self.EDGE):
            for j in range(self.EDGE):
                if self.grid_data[i][j] == self.WHITE:
                    white_count += 1
                elif self.grid_data[i][j] == self.BLACK:
                    black_count += 1
        if not (white_count and black_count):
            return True


'''
    def grid_check(self, i, j):
        if self.grid_data[i][j] == self.piece:
            return True


    def around_check(self, i, j, n, m):
        if (n != 0 or m != 0) and (0 <= i+n <= self.EDGE-1 and 0 <= j+m <= self.EDGE-1):
            if self.grid_data[i+n][j+m] == self.piece:
                return True


    def result(self, i, j, n, m):
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
                            if self.around_check(i, j, n, m):
                                if self.result(i, j, n, m):
                                    return True
'''


class TUIBoard(Board):

    def input_(self):
        re = False
        emp = True

        while True:
            self.show()
            if re:
                print("1 ~", self.EDGE, "で入力してください。")
            elif not emp:
                print("そのマスは空いていません。")
            else:
                print()
            print("You :", self.PIECE[self.piece])

            re = False
            emp = True

            x = input("X = ")
            if x in self.ALLOWED_NUMBERS:
                x = int(x)-1
            else:
                re = True
                continue

            y = input("Y = ")
            if y in self.ALLOWED_NUMBERS:
                y = int(y)-1
            else:
                re = True
                continue
            
            if self.grid_data[y][x] != self.EMPTY:
                emp = False
                continue
            else:
                return x, y

    
    def result(self):
        self.show()
        print(f"\n")


        
board = TUIBoard()
turn = 0
while True:
    board.piece *= -1
    turn += 1

    x, y = board.input_()
    board.set_(x, y)
    board.trun(x, y)
    if turn == board.EDGE**2-4 or board.piece_count():
        break
