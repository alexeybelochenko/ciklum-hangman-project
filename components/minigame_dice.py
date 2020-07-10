class A:
    def __init__(self):
        self.Aa = 0
        self.B = 1


class B(A):
    def f(self):
        print(self.Aa)


B().f()