class Player:
    def __init__(self):
        self.left = 1
        self.right = 1

    def transport(self, number):
        self.left += number
        self.transport = number

one_man = Player()
two_man = Player()
one_man.transport(2)


input(f"{} or {}")


class A:

    b = 1

    def test(self):
        ...
A.b

a = A()
a.test()
print(a.b) # 1
A.b = 2
print(a.b) # 2



