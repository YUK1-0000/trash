DOT = "."
SPACE = " "
n = 50

def f(x):
    return x**3+10

def graph():
    for y in reversed(range(n)):
        for x in map(lambda i:i/2, range(n*2)):
            print(DOT if -1<=f(x)-y<=1 else SPACE, end="")
        print()

graph()