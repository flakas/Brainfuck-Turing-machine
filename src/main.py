import BrainfuckMachine 

machine = BrainfuckMachine.BrainfuckMachine()
f = open('helloworld.bf', 'r')
machine.setCode(f.read())
f.close()
machine.run()
