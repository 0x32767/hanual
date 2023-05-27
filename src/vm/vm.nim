#[
Nim VM, Virtual machine for compiling and interepreting the hanual bytecode. It is speedy as nim is complied to C.
!! DO NOT CHANGE THIS UNLESS YOU KNOW WHAT YOU'RE DOING !!

        # Notes on bytecode

        NOP = 0b0000_0000,
    
        JMP = 0b1110_0000,  # unconditional Jump
        JEZ = 0b1110_0001,  # Jump if 0
        JNZ = 0b1110_0010,  # Jump not 0
        JIE = 0b1110_0011,  # jump if error
    
        SWP = 0b0100_1000,  # swap top two elements
        YNK = 0b1100_1100,  # yank n'th element and push it to top
    
        PP1 = 0b0100_0000,  # Pops top element
        PP2 = 0b0100_0001,  # Pops two elements of stack
        PP3 = 0b0100_0010,  # pops three elements of stack
    
        PGV = 0b1100_0000,  # Push global value on stack
        PGC = 0b1100_0001,  # Push constant onto stack
        PGA = 0b1100_0010,  # Push global address, e.g. function
    
        PK2 = 0b0100_0010,  # Pack top 2 elements into tuple
        PK3 = 0b0100_0011,  # Pack top 3 elements into tuple
        PK4 = 0b0100_0100,  # Pack top 4 elements into tuple
        PK5 = 0b0100_0101,  # Pack top 5 elements into tuple
        PKN = 0b1100_1000,  # Pack top n elements into tuple
        PK1 = 0b0100_1001,  # Pack first value into tuple, (I forgot to add this in earlier, so now it exists)
    
        RZE = 0b0100_0000,  # Raise Exception
        
        CAL = 0b0100_0001,  # Call function
        RET = 0b0000_0001  # return

        # File extension (Not related to chenobal)
        .chnl

        # Docs links
        https://nim-lang.org/docs/manual.html#exception-handling
        https://nim-lang.org/docs/manual.html#statements-and-expressions-while-statement
        https://nim-lang.org/docs/os.html
        https://nim-lang.org/docs/tut2.html#exceptions-raise-statement
        https://stackoverflow.com/questions/34427858/reading-bytes-from-many-files-performance
]#

# Imports
import os
import std/os

# Parse file into various parts (Instruction, const, etc. pools)
var
    f: File
    end: False

if open(f, "main.chnl"):
    while end != True:
        for instructions in f:
            ...
else:
    raise "The main file does not exist, please create one."    

for instructions in somerandomfile:
    instructions.NOP