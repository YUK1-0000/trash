from typing import Any


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
        "駒を置く。"
        self.grid_data[Y][X] = self.turn
        
    def show(self)  -> None:
        "ボードを表示します。"
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

    def trial(self) -> bool:
        "ゲーム終了かどうかを返す。"
        any((self.grid_data[Y+i][X+j] == self.EMPTY for j in range(self.edge)) for i in range(self.edge)) 



board = Board()

while True:
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
                print(board.grid_data)
                break
        else:
            print("1 ~", board.edge, "で入力してください。")