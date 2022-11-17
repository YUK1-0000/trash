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
    BREAK = False
    for l in (-1, 1):
            for i in range(board.edge):
                for j in range(board.edge):
                    if board.grid_data[i][j] == l:
                        for n in (-1, 0, 1):
                            for m in (-1, 0, 1):
                                if 0 <= i+n <= board.edge-1 and 0 <= j+m <= board.edge-1:
                                    if board.grid_data[i+n][j+m] == l:
                                        count = 2
                                        for t in range(board.edge):
                                            if 0 <= i+n*(t+2) <= board.edge-1 and 0 <= j+m*(t+2) <= board.edge-1:
                                                if board.grid_data[i+n*(t+2)][j+m*(t+2)] == l:
                                                    count += 1
                                                    if count >= board.edge:
                                                        if l == 1:
                                                            print("o WIN")
                                                        else:
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
        