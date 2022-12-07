class Board:
    EDGE = 8
    WIN_REACH = 3
    PIECE = ("-", "○", "●")
    WHITE = 1
    BLACK = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(EDGE)]
    AXIS = [" "] + [i+1 for i in range(10)]


    def __init__(self):
        self.grid_data = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        self.grid_data[3][3], self.grid_data[4][4] = self.BLACK, self.BLACK
        self.grid_data[4][3], self.grid_data[3][4] = self.WHITE, self.WHITE
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


    def turn(self, x, y):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if 0 <= y+i < self.EDGE and 0 <= x+j < self.EDGE:
                    if self.grid_data[y+i][x+j] == self.piece*-1:
                        # print(f"o  y {1+y+i}  x {1+x+j}")
                        count = 1
                        for n in range(self.EDGE):
                            if 0 <= y+i*(n+1) < self.EDGE and 0 <= x+j*(n+1) < self.EDGE:
                                if self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.EMPTY:
                                    break
                                elif self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece*-1:
                                    count += 1
                                    # print(f"1  y {1+y+i*(n+1)}  x {1+x+j*(n+1)}")
                                elif self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece:
                                    for m in range(count):
                                        # print(f"2  y {1+y+i*(m+1)}  x {1+x+j*(m+1)}")
                                        self.grid_data[y+i*(m+1)][x+j*(m+1)] = self.piece
                                    break


    def turn_check(self, x, y):
        if self.grid_data[y][x] == self.EMPTY:
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if 0 <= y+i < self.EDGE and 0 <= x+j < self.EDGE:
                        if self.grid_data[y+i][x+j] == self.piece*-1:
                            count = 1
                            for n in range(self.EDGE):
                                if 0 <= y+i*(n+1) < self.EDGE and 0 <= x+j*(n+1) < self.EDGE:
                                    if self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece*-1:
                                        count += 1
                                    elif self.grid_data[y+i*(n+1)][x+j*(n+1)] == self.piece:
                                        return True


    def turn_check_all(self):
        for y in range(self.EDGE):
            for x in range(self.EDGE):
                if self.turn_check(x, y):
                    return True


    def piece_count(self):

        piece_count = 0
        white_count = 0
        black_count = 0

        for i in range(self.EDGE):
            for j in range(self.EDGE):

                match self.grid_data[i][j]:
                    case 1:
                        piece_count += 1
                        white_count += 1
                    case -1:
                        piece_count += 1
                        black_count += 1

        return piece_count, white_count, black_count


class TUIBoard(Board):

    def input_(self):

        re = False
        emp = True
        turn = True

        while True:

            self.show()
            if re:
                print(f"{self.AXIS[1]} ~ {self.AXIS[self.EDGE]}で入力してください。")
            elif not emp:
                print("そのマスは空いていません。")
            elif not turn:
                print("返せる駒がありません。")
            else:
                print()
            print("You :", self.PIECE[self.piece])

            re = False

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
            
            emp = True
            turn = True

            if self.grid_data[y][x] != self.EMPTY:
                emp = False
                continue
            elif not self.turn_check(x, y):
                turn = False
                continue
            else:
                return x, y

    def pass_(self):
        self.show()
        print("エンターでパス。")
        print("You :", self.PIECE[self.piece])
        input()


    def result(self):
        self.show()
        print(f"\n{board.PIECE[board.WHITE]}{white_count} {board.PIECE[board.BLACK]}{black_count}")


        
board = TUIBoard()
turn = 0
while True:
    
    turn += 1

    if board.turn_check_all():
        x, y = board.input_()
        board.set_(x, y)
        board.turn(x, y)
    else:
        board.pass_()

    piece_count, white_count, black_count = board.piece_count()
    if not (white_count and black_count) or (piece_count == board.EDGE**2):
        break

board.result()