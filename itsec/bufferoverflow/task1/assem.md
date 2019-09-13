Dump of assembler code for function main:  

   0x00000000004005e0 <+0>:     push   %rbp								# init  
   0x00000000004005e1 <+1>:     mov    %rsp,%rbp  
   0x00000000004005e4 <+4>:     sub    $0x40,%rsp  
   0x00000000004005e8 <+8>:     movl   $0x0,-0x4(%rbp)  
   0x00000000004005ef <+15>:    mov    %edi,-0x8(%rbp)  
   0x00000000004005f2 <+18>:    mov    %rsi,-0x10(%rbp)  
   0x00000000004005f6 <+22>:    cmpl   $0x3,-0x8(%rbp)  
   0x00000000004005fd <+29>:    je     0x400628 <main+72>				# jump if equal, <main+72> =  movl   $0x0,-0x14(%rbp)  
   0x0000000000400603 <+35>:    lea    0x4007cc,%rdi  
   0x000000000040060b <+43>:    mov    -0x10(%rbp),%rax  
--   --    
   0x000000000040060f <+47>:    mov    (%rax),%rsi  
   0x0000000000400612 <+50>:    mov    $0x0,%al
   0x0000000000400614 <+52>:    callq  0x4004d0 <printf@plt>			# call printf  
   0x0000000000400619 <+57>:    movl   $0x1,-0x4(%rbp)  
   0x0000000000400620 <+64>:    mov    %eax,-0x2c(%rbp)  
   0x0000000000400623 <+67>:    jmpq   0x4006cf <main+239>				# return to main  
   0x0000000000400628 <+72>:    movl   $0x0,-0x14(%rbp)  
   0x000000000040062f <+79>:    mov    -0x10(%rbp),%rax  
   0x0000000000400633 <+83>:    mov    0x8(%rax),%rdi  
   0x0000000000400637 <+87>:    callq  0x4004c0 <strlen@plt>			# call strlen  
   0x000000000040063c <+92>:    cmp    $0x8,%rax						# compare st strlen to 8  
   0x0000000000400642 <+98>:    jne    0x400679 <main+153>				# return to main  
   0x0000000000400648 <+104>:   lea    0x4007e9,%rsi  
   0x0000000000400650 <+112>:   movabs $0x8,%rdx  
   0x000000000040065a <+122>:   mov    -0x10(%rbp),%rax  
   0x000000000040065e <+126>:   mov    0x8(%rax),%rdi  
   0x0000000000400662 <+130>:   callq  0x4004a0 <strncmp@plt>			# call strncmp  
   0x0000000000400667 <+135>:   cmp    $0x0,%eax  
   0x000000000040066c <+140>:   jne    0x400679 <main+153>				# return to main  
   0x0000000000400672 <+146>:   movl   $0x1,-0x14(%rbp)  
   0x0000000000400679 <+153>:   lea    -0x28(%rbp),%rdi  
--   --  
   0x000000000040067d <+157>:   mov    -0x10(%rbp),%rax  
   0x0000000000400681 <+161>:   mov    0x10(%rax),%rsi  
   0x0000000000400685 <+165>:   callq  0x4004b0 <strcpy@plt>			# call strcpy  
   0x000000000040068a <+170>:   cmpl   $0x0,-0x14(%rbp)  
   0x0000000000400691 <+177>:   mov    %rax,-0x38(%rbp)  
   0x0000000000400695 <+181>:   je     0x4006b6 <main+214>				# return to main  
   0x000000000040069b <+187>:   lea    0x4007f2,%rdi  
   0x00000000004006a3 <+195>:   lea    -0x28(%rbp),%rsi  
   0x00000000004006a7 <+199>:   mov    $0x0,%al  
   0x00000000004006a9 <+201>:   callq  0x4004d0 <printf@plt>			# call printf  
   0x00000000004006ae <+206>:   mov    %eax,-0x3c(%rbp)  
   0x00000000004006b1 <+209>:   jmpq   0x4006c8 <main+232>				# return to main  
   0x00000000004006b6 <+214>:   lea    0x400817,%rdi  
   0x00000000004006be <+222>:   mov    $0x0,%al
   0x00000000004006c0 <+224>:   callq  0x4004d0 <printf@plt>			# call printf  
   0x00000000004006c5 <+229>:   mov    %eax,-0x40(%rbp)  
   0x00000000004006c8 <+232>:   movl   $0x0,-0x4(%rbp)  
   0x00000000004006cf <+239>:   mov    -0x4(%rbp),%eax  
   0x00000000004006d2 <+242>:   add    $0x40,%rsp  
   0x00000000004006d6 <+246>:   pop    %rbp  
   0x00000000004006d7 <+247>:   retq   									# return to main  
