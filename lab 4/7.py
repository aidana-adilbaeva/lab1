#reverse iterator
class reverse:
    def __init__(self, s):
        self.s = s
        self.index = len(s) - 1
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.s[self.index]
        self.index -= 1
        return char
        
s = input()
rev = reverse(s)
for i in rev:
    print(i, end="")