class BrainfuckMachine:
    """Brainfuck interpreter"""

    def __init__(self):
        self.tape = [0 for i in range(30000)]
        self.cellPointer = 0
        self.codePointer = 0
        self.code = ''
        self.loopTree = []

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
        elif(c in ['[', ']']):
            self.loop()
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
        print chr(self.tape[self.cellPointer]),
        return

    def getPointer(self):
        c = raw_input("Enter a character: ")
        self.tape[self.cellPointer] = ord(c[0])
        return

    def loop(self):
        if(self.code[self.codePointer] == '['):
            if(self.tape[self.cellPointer] == 0):
                self.codePointer = self.findMatchingBrace()
            elif(self.tape[self.cellPointer] != 0):
                return
        elif(self.code[self.codePointer] == ']'):
            if(self.tape[self.cellPointer] == 0):
                return
            elif(self.tape[self.cellPointer] != 0):
                self.codePointer = self.findMatchingBrace()
        return

    def findMatchingBrace(self):
        position = self.codePointer
        level = 0
        if(self.code[position] == ']'):
            direction = -1
            position += direction
            while self.code[position] != '[' or level != 0:
                if(self.code[position] == ']'):
                    level += 1
                elif(self.code[position] == '['):
                    level -= 1
                position += direction
        else:
            direction = 1
            position += direction
            while self.code[position] != ']' or level != 0:
                if(self.code[position] == '['):
                    level += 1
                elif(self.code[position] == ']'):
                    level -= 1
                position += direction
        return position

if __name__ == "__main__":
    """If used directly, run from command line"""
    import sys
    machine = BrainfuckMachine()
    machine.setCode(sys.argv[1])
    machine.run()
