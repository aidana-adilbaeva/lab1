class StringHandler:
    def getString(self, string):
        self.string = string

    def printString(self):
        print(self.string.upper())

string = input()
handler = StringHandler()
handler.getString(string)
handler.printString()