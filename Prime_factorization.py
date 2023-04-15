n = int(input())

def a(x):
    if x <= 1:
        return
    for i in range(2, x + 1):
        if x % i == 0:
            print(i)
            return a(int(x / i))

a(n)