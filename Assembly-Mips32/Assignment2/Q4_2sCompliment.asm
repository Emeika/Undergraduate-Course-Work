.data
	prompt: .asciiz "Enter Integer (1 to 15): "
	output: .asciiz "2's compliment: "
	
.text 
	li $v0, 4         # Load system call code for printing string
	la $a0, prompt    # Load the address of prompt variable into register $a0
	syscall           # Call system call to print string
	
	li $v0, 5         # Read the integer into $t0
	syscall
	move $t0, $v0
	
	
	li $t1, 15        # -1 is equivalent to all 1's in binary (0xffffffff)
	xor $t2, $t0, $t1  # Do the compliment 
	
	add $t2, $t2, 1
	
	li $v0, 4    	  # Print the output string 
	la $a0, output
	syscall
	
	li $v0, 1	  # Print the inetger
	move $a0, $t0
	syscall
		
	li $v0, 10    # Exit
	syscall
