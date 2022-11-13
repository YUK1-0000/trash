class Board:
    edge = 8
    WHITE = 1
    BLACK = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(edge)]
    AXIS = ("０", "１", "２", "３", "４", "５", "６" ,"７", "８")
    def __init__(self)  -> None:
        self.grid_data = [[0 for _ in range(8)] for _ in range(8)]
        self.grid_data[3][3] = self.grid_data[4][4] = self.WHITE
        self.grid_data[3][4] = self.grid_data[4][3] = self.BLACK
        self.turn = -1
        
    def set_(self)  -> None:
        "駒を置く。"
        self.turn_pieces = 0

        while True:
            X = input("X = ")
            Y = input("Y = ")
            if X in self.ALLOWED_NUMBERS and Y in self.ALLOWED_NUMBERS:
                X, Y = int(X)-1, int(Y)-1
                if self.grid_data[Y][X] != self.EMPTY:
                    print("既に駒があります。")
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= Y+i <= self.edge-1 and 0 <= X+j <= self.edge-1:
                            if self.grid_data[Y+i][X+j] == self.turn*-1:
                                for n in range(self.edge):
                                    if 0 <= Y+i*(n+1) <= self.edge-1 and 0 <= X+j *(n+1) <= self.edge-1:
                                        if self.grid_data[Y+i*(n+1)][X+j*(n+1)] == self.turn*-1:
                                            self.turn_pieces += 1
                                        elif self.grid_data[Y+i*(n+1)][X+j*(n+1)] == self.turn and self.turn_pieces > 0:
                                            for m in range(self.turn_pieces):
                                                self.grid_data[Y+i*m][X+j*m] = self.turn
                                            break
                break
            else:
                print("1~8で入力してください。")
        
    def show(self)  -> None:
        "ボードを表示します。"
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(self.edge+1):
            print(self.AXIS[i], end = "")
        print()
        for i in range(self.edge):
            print(self.AXIS[i+1], end = "")
            for j in range(self.edge):
                if self.grid_data[j][i] == self.BLACK:
                    print("黒", end = "")
                elif self.grid_data[j][i] == self.WHITE:
                    print("白", end = "")
                else:
                    print("＋", end = "")      
            print()


def trial(self)  -> bool:
        "ゲーム終了かどうかを返す。"

class WindowBoard(Board):
    def computer(self)  -> None:
        "コンピューターにやらせます。"

    def show(self)  -> None:
        "ウィンドウでボードを表示します。"




board = Board()
board.turn  *=  -1
while True:
    board.show()
    board.set_()