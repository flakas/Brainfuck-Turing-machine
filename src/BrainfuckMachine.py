
class BrainfuckMachine:
    """Brainfuck interpreter"""

    def __init__(self):
        self.tape = [0 for i in range(30000)]
        self.cellPointer = 0
        self.codePointer = 0
        self.code = ''

    def setCode(self, code):
        self.code = code
        self.codeLength = len(self.code) - 1

    def run(self):
        self.codePointer = 0
        while self.codePointer < self.codeLength:
            self.doStep()
        return
    
    def doStep(self):
        c = self.code[self.codePointer]
        if(c == '+'):
            self.changeValue(1)
        elif(c == '-'):
            self.changeValue(-1)
        elif(c == '>'):
            self.movePointer(1)
        elif(c == '<'):
            self.movePointer(-1)
        elif(c == '.'):
            self.printPointer()
        elif(c == ','):
            self.getPointer()
        self.moveCodePointer(1)
        return 

    def movePointer(self, direction):
        """Moves pointer to the proper direction"""
        self.cellPointer += direction
        return
    
    def moveCodePointer(self, direction):
        """Moves code pointer to proper direction"""
        self.codePointer += direction
        return

    def changeValue(self, action):
        self.tape[self.cellPointer] += action
        return

    def printPointer(self):
        print self.tape[self.cellPointer],
        return

    def getPointer(self):
        c = raw_input("Enter a character: ")
        self.tape[self.cellPointer] = ord(c[0])
        return

    def loop(self):
        return