# Brainfuck Turing machine #

## What is Brainfuck? ##
http://en.wikipedia.org/wiki/Brainfuck

Brainfuck is an esoteric programming language, it's noted for its extreme minimalism.
It was not made to be suitable for practical use, but it's designed to challenge and 
amuse programmers.

* `>` Increase the data pointer
* `<` Decrease the data pointer
* `+` Increment the byte at the data pointer
* `-` Decrement the byte at the data pointer
* `.` Output a character, the ASCII value of which being the byte at the data pointer
* `,` Accept one byte of input, storing its value in the byte at the data pointer
* `[` If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after matching `]` command
* `]` If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching `[` command

## What is Turing machine? ##
http://en.wikipedia.org/wiki/Turing_machine

Turing machine is a device that manipulates symbols on a strip of tape to a table of rules. 
Even though it is simple, a Turing machine can be adapted to simulate the logic of any computer 
algorithm, and is particularly useful in explaining the functions of a CPU inside a computer.

## Installation ##

None required!

## Contribute ##

If you want to get involved, fork the project, make changes and submit a pull request!

## LICENSE ##

What? Do whatever you want with it
