class Board:
    edge = 3
    PIECE = ("", "o", "x")
    MARU = 1
    BATSU = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(edge)]
    AXIS = ("0", "1", "2", "3", "4", "5", "6" ,"7", "8", "9")
    def __init__(self):
        self.grid_data = [[0 for _ in range(self.edge)] for _ in range(self.edge)]
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
                print("1 ~", board.edge, "で入力してください。")        

    def set_(self, X, Y):
        self.grid_data[Y][X] = self.piece
        
    def show(self):
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

        




board = Board()
BREAK = False
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
            print("1 ~", board.edge, "で入力してください。")

    board.set_(X, Y)

    for i in range(board.edge):
        for j in range(board.edge):
            if board.grid_data[i][j] == board.piece:
                for n in (-1, 0, 1):
                    for m in (-1, 0, 1):
                        if (n != 0 or m != 0) and (0 <= i+n <= board.edge-1 and 0 <= j+m <= board.edge-1):
                            if board.grid_data[i+n][j+m] == board.piece:
                                count = 1
                                for t in range(board.edge):
                                    if 0 <= i+n*(t+1) <= board.edge-1 and 0 <= j+m*(t+1) <= board.edge-1:
                                        if board.grid_data[i+n*(t+1)][j+m*(t+1)] == board.piece:
                                            count += 1
                                            if BREAK:
                                                break
                                            elif count == board.edge:
                                                board.show()
                                                print("\n", board.PIECE[board.piece], "WIN")
                                                BREAK = True
                                            elif turn == board.edge**2:
                                                board.show()
                                                print("\nDRAW")
                                                BREAK = True