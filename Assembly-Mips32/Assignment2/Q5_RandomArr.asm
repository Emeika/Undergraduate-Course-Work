.data
     Arr: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
     msg: .asciiz "The sum of elements with odd indices is: "
.text
     la $s0, Arr          # load base address of array into $s0
     li $s1, 20           # set loop counter to length of array
     li $t0, 0            # initialize sum to 0
    
loop:
     lw $t1, 4($s0)       # load the value of the current element into $t1
     addi $s0, $s0, 8     # increment pointer to next element
     addi $s1, $s1, -2    # decrement loop counter by 2 (skip even indices)
     add $t0, $t0, $t1    # add current element to sum
    
     bgtz $s1, loop       # branch to loop if loop counter is greater than zero

     # print the sum of elements with odd indices
     li $v0, 4            # load system call code for printing string
     la $a0, msg          # load address of message string into $a0
     syscall              # print message string
     li $v0, 1            # load system call code for printing integer
     move $a0, $t0        # move sum to $a0
     syscall              # print sum
     li $v0, 10           # load system call code for exit
     syscall              # exit program
