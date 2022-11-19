class Board:
    edge = 3
    MARU = 1
    BATSU = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(edge)]
    AXIS = ("0", "1", "2", "3", "4", "5", "6" ,"7", "8", "9")
    def __init__(self)  -> None:
        self.grid_data = [[0 for _ in range(self.edge)] for _ in range(self.edge)]
        self.turn = -1
        
    def set_(self)  -> None:
        self.grid_data[Y][X] = self.turn
        
    def show(self)  -> None:
        self.grid = [[0 for _ in range(self.edge)] for _ in range(self.edge)]
        for i in range(self.edge+1):
            print(self.AXIS[i], end = " ")
        print()
        for i in range(self.edge):
            print(self.AXIS[i+1], end = " ")
            for j in range(self.edge):
                if self.grid_data[i][j] == self.BATSU:
                    print("x", end = " ")
                elif self.grid_data[i][j] == self.MARU:
                    print("o", end = " ")
                else:
                    print(" ", end = " ")      
            print()

    def trial(self):
        for i in range(self.edge):
                for j in range(self.edge):
                    if self.grid_data[i][j] == self.turn:
                        for n in (-1, 0, 1):
                            for m in (-1, 0, 1):
                                if n != 0 and m != 0 and 0 <= i+n <= self.edge-1 and 0 <= j+m <= self.edge-1:
                                    if self.grid_data[i+n][j+m] == self.turn:
                                        count = 0
                                        for t in range(self.edge):
                                            if 0 <= i+n*t <= self.edge-1 and 0 <= j+m*t <= self.edge-1:
                                                if self.grid_data[i+n*t][j+m*t] == self.turn:
                                                    count += 1
                                                    if count == self.edge:
                                                        if self.turn == 1:
                                                            self.show()
                                                            print("o WIN")
                                                        else:
                                                            self.show()
                                                            print("x WIN")
                                                        BREAK = True
                                                        break
                                        if BREAK:
                                            break
                            if BREAK:
                                break
                        if BREAK:
                            break
                if BREAK:
                    break
        if BREAK:
            break

        




board = Board()
BREAK = False
while BREAK == False:
    board.show()
    board.turn *= -1
    if board.turn == 1:
        print("You : o")
    else:
        print("You : x")
    while True:
        X = input("X = ")
        Y = input("Y = ")
        if X in board.ALLOWED_NUMBERS and Y in board.ALLOWED_NUMBERS:
            X, Y = int(X)-1, int(Y)-1
            if board.grid_data[Y][X] != board.EMPTY:
                print("そのマスは空いていません。")
            else:
                board.set_()
                break
        else:
            print("1 ~", board.edge, "で入力してください。")
    empty_count = board.edge**2
    for i in range(board.edge):
            for j in range(board.edge):
                if board.grid_data[j][i] != board.EMPTY:
                    empty_count -= 1
                else:
                    if board.grid_data[i][j] == board.turn:
                        for n in (-1, 0, 1):
                            for m in (-1, 0, 1):
                                if n != 0 and m != 0 and 0 <= i+n <= board.edge-1 and 0 <= j+m <= board.edge-1:
                                    if board.grid_data[i+n][j+m] == board.turn:
                                        count = 0
                                        for t in range(board.edge):
                                            if 0 <= i+n*t <= board.edge-1 and 0 <= j+m*t <= board.edge-1:
                                                if board.grid_data[i+n*t][j+m*t] == board.turn:
                                                    count += 1
                                                    if count == board.edge:
                                                        if board.turn == 1:
                                                            board.show()
                                                            print("o WIN")
                                                        else:
                                                            board.show()
                                                            print("x WIN")
                                                        BREAK = True
                                                        break
                                        if BREAK:
                                            break
                            if BREAK:
                                break
                        if BREAK:
                            break
            if BREAK:
                break
    if BREAK:
        break
    elif empty_count == 0:
        board.show()
        print("DRAW")
        break