class A:
    def __init__(self):
        print("A")
        print("a")

class B:
    def __init__(self):
        print("B")
        print("b")

class C(A):
    def __init__(self):
        print("C")
        super().__init__()
        print("c")

class D(B):
    def __init__(self):
        print("D")
        super().__init__()
        print("d")

class E(A, B):
    def __init__(self):
        print("E")
        super().__init__()
        print("e")

class F(D, E):
    def __init__(self):
        print("F")
        super().__init__()
        print("f")
