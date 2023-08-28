.data
	expression: .asciiz "a. x = y + z + 10\n"
	y: .asciiz "Enter y: "
	z: .asciiz "Enter z: "
	x: .word 0
	asum: .asciiz "x= "
	
	newline: .asciiz "\n"
	
	expression2: .asciiz "b. a = (b - 3) + 2c\n"
	b: .asciiz "Enter b: "
	c: .asciiz "Enter c: "
	a: .word 0
	bsum: .asciiz "a= "
	
	


.text
	li $v0, 4      # Print expression
	la $a0, expression
	syscall
	
	li $v0, 4     # Print Prompt to enter y
	la $a0, y
	syscall 
	
	li $v0, 5     # Read Integer y to $t0
	syscall
	move $t0, $v0
	
	li $v0, 4     # Print Prompt to enter z
	la $a0, z
	syscall 
	
	li $v0, 5     # Read Integer z to $t1
	syscall
	move $t1, $v0
	
	add $t0, $t0, $t1   # Add y + z
	add $t0, $t0, 10    # Add sum with 10
	
	sw $t0, x           # Store sum into varibale x
	
	li $v0, 4           #Print variable X
	la $a0, asum
	syscall
	
	li $v0, 1           # Print Integer calculated X value 
	lw $s1, x           # Load x value to register $s1
	move $a0, $s1
	syscall
	
	li $v0, 4       # Load system call code for printing string
	la $a0, newline  # Load the address of the newline character into register $a0
	syscall         # Call system call to print string
	
	# b
	
	li $v0, 4      # Print expression 2
	la $a0, expression2
	syscall
	
	li $v0, 4     # Print Prompt to enter b
	la $a0, b
	syscall
	
	li $v0, 5     # Read Integer b to $t0
	syscall
	move $t0, $v0
	
	li $v0, 4     # Print Prompt to enter c
	la $a0, c
	syscall
	
	li $v0, 5     # Read Integer c to $t1
	syscall
	move $t1, $v0
	
	sub $t0, $t0, 3    # (b – 3)
	
	add $t2, $t1, $t1  # c * 2
	
	add $t0, $t0, $t2  # Accumulate the above
	
	sw $t0, a          # Store sum to variable a
	
	li $v0, 4          #Print variable A
	la $a0, bsum
	syscall
	
	li $v0, 1     # Print Integer calculated a value 
	lw $s1, a     # Load a value to register $s1
	move $a0, $s1
	syscall
	
	li $v0, 10    # Exit
	syscall
	
	
	
	
	
