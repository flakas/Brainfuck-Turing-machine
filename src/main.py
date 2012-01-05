import BrainfuckMachine 

machine = BrainfuckMachine.BrainfuckMachine(50)
f = open('helloworld.bf', 'r')
machine.setCode(f.read())
f.close()
machine.run()
print machine.getOutput()
