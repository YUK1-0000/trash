player = [[i+1 for i in range(13)] for _ in range(4)]
for i in range(4):
    print(" ".join(map(str, player[i])))