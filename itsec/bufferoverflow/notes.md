# Processes
                             /------------------\  lower
                             |                  |  memory
                             |       Text       |  addresses
                             |                  |
                             |------------------|
                             |   (Initialized)  |
                             |        Data      |
                             |  (Uninitialized) |
                             |------------------|
                             |                  |
                             |       Stack      |  higher
                             |                  |  memory
                             \------------------/  addresses
- Text = code (instructions) + Read only data
- Stack = LIFO -> push, pop 

# Stack and Buffer Overflow
- contiguous block of memory that grows down most of the time 
- special register **SP** is called Stack Pointer and points to the top of the stack
- memory can only be address in multiples of the **word size**, e.g. 4 bytes or 32 bit.

```c
char buffer1[5];
char buffer2[10];
```
- in this program there will be ceil(5/4) + ceil(10/4) = 5 * WORD_SIZE = 20 Bytes
- so after a function call, to a function `function(int a, int b, int c);` that allocates those two buffers, the memory will look like this:
- **Hint:** If we look at buffer1 and image that we put more that 8 bytes into it, we can imagine, that we might be able to **override** the ret address
 
<------   \[    buffer2          ]\[    buffer1       ]\[  sfp  ]\[  ret  ]\[  a  ]\[  b  ]\[ c   ]  



- if we look at **example1**, compile it and then disassemble it's main method, we will see, something similar to :

------------------------------------------------------------------------------
[aleph1]$ gdb a.out  
(gdb) disassemble main  
Dump of assembler code for function main:  
0x8000490 <main>:       pushl  %ebp  
0x8000491 <main+1>:     movl   %esp,%ebp  
0x8000493 <main+3>:     subl   $0x4,%esp  
0x8000496 <main+6>:     movl   $0x0,0xfffffffc(%ebp)  
0x800049d <main+13>:    pushl  $0x3 					# here the three variables are pushed onto the stack  
0x800049f <main+15>:    pushl  $0x2  
0x80004a1 <main+17>:    pushl  $0x1  
0x80004a3 <main+19>:    call   0x8000470 <function> 	# here the function gets called  
0x80004a8 <main+24>:    addl   $0xc,%esp				# here we see the RET  
0x80004ab <main+27>:    movl   $0x1,0xfffffffc(%ebp)  
0x80004b2 <main+34>:    movl   0xfffffffc(%ebp),%eax  
0x80004b5 <main+37>:    pushl  %eax  
0x80004b6 <main+38>:    pushl  $0x80004f8  
0x80004bb <main+43>:    call   0x8000378 <printf>  
0x80004c0 <main+48>:    addl   $0x8,%esp  
0x80004c3 <main+51>:    movl   %ebp,%esp  
0x80004c5 <main+53>:    popl   %ebp  
0x80004c6 <main+54>:    ret  
0x80004c7 <main+55>:    nop  
------------------------------------------------------------------------------

# Shell Code aka where the magic happens

- We can change the RET, but we somehow need to insert our own code into the program
- We do that, by including our code into the buffer itself and overriding the RET with the addr of the newly inserted code

<------   \[SSSSSSSSSSSSSSSSSSSS]\[SSSS]\[0xD8]\[0x01]\[0x02]\[0x03]  
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^  
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |___________________________________|  

- we need to let RET point to the beginning of S, e.g. 
