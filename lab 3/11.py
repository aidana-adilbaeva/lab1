class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other_pair):
        a_sum = self.a + other_pair.a
        b_sum = self.b + other_pair.b
        print(f"Result: {a_sum} {b_sum}")

a1, b1, a2, b2 = map(int, input().split())

pair = Pair(a1, b1)
other_pair = Pair(a2, b2)

pair.add(other_pair)