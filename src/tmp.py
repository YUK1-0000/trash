      while True:
            while True:
                X = input("X = ")
                Y = input("Y = ")
                if X in self.ALLOWED_NUMBERS and Y in self.ALLOWED_NUMBERS:
                    X, Y = int(X)-1, int(Y)-1
                    break
                else:
                    print("1~8で入力してください。")
            if self.grid[Y][X] == self.EMPTY:
                break
            else:
                print("入力された座標は既に埋まっています。")