def a(a):
    if a == 1:
        print(a)
        return 1, 2

b = 1

if a(b):
    print("o")
elif not a(b):
    print("x")