.data
	prompt: .asciiz "Enter 2 numbers: "
	output: .asciiz "Swapped numbers are : "
	newline: .asciiz "\n"
	


.text

	li $v0, 4   #Print prompt
	la $a0, prompt
	syscall
	
	li $v0, 5   # Read integer into t0
	syscall
	move $t0, $v0
	
	li $v0, 5    #Read 2nd integer into t1
	syscall
	move $t1, $v0
	
	xor $t0, $t0, $t1
	xor $t1, $t0, $t1
	xor $t0, $t0, $t1
	
	li $v0, 4
	la $a0, output
	syscall
	
	li $v0, 1
	move $a0, $t0
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	li $v0, 1
	move $a0, $t1
	syscall
	
	li $v0, 10
	syscall
	
	

	
	