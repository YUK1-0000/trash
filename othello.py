class Board:
    EDGE = 8
    PIECE = (" ", "○", "●")
    WHITE = 1
    BLACK = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(EDGE)]
    AXIS = [i for i in range(9)]


    def __init__(self):
        self.grid_data = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        self.grid_data[3][3] = self.grid_data[4][4] = self.WHITE
        self.grid_data[3][4] = self.grid_data[4][3] = self.BLACK
        self.piece = -1


    def input(self):
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
            


    def set(self, x, y):
        self.grid_data[y][x] = self.piece


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

######
    def around_check(self, x, y, i, j):
        if 0 <= y+i <= self.EDGE-1 and 0 <= x+j <= self.EDGE-1:
            if self.grid_data[y+i][x+j] == self.piece*-1:
                return True


    def count(self, x, y, i, j, count):
        for n in range(self.EDGE):
            if self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece*-1:
                count += 1
            elif self.grid_data[y+i*(n+1)][x+j*(n+1)] != self.piece*-1:
                return 



    
    def count(self, i, j, n, m):
        count = 1
        for t in range(self.EDGE):
            if 0 <= i+n*(t+1) <= self.EDGE-1 and 0 <= j+m*(t+1) <= self.EDGE-1:
                if self.grid_data[i+n*(t+1)][j+m*(t+1)] == self.piece:
                    count += 1
                else:

                    
######
    

    def turn(self, x, y):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):

                if 0 <= y+i <= self.EDGE-1 and 0 <= x+j <= self.EDGE-1:
                    if self.grid_data[y+i][x+j] == self.piece*-1:

                        count = 1
                        for n in range(self.EDGE):
                            if self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece*-1:
                                count += 1
                            elif self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece:
                                for m in range(count):
                                    self.set(x, y)

                        
                        


                    

board = Board()
turn = 0
while True:
    board.piece *= -1
    turn += 1

    x, y = board.input()
    board.set(x, y)
    if board.turn(x, y):
        break