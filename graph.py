r = 50
dot = "."
space = " "

a, b, c, d = map(int, input().split())

for y in reversed(range(r)):
    for x in map(lambda i: i/2, range(r*2)):
        print(dot if y-2 <= a*x**3 + b*x**2 + c*x + d <= y+2 else space, end="")
    print()
    
'''
def tdf(x) -> int:
    return a*x**2+b*x+c

x = r
while x <= 0:
    x -= 0.1
_    tdf(x)
    print(dot if r  else space, end="")'''