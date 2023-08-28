.data
	prompt: .asciiz "Enter 3 numbers: "
	greater: .asciiz "Sum is greater than 10. "
	less: .asciiz "Sum is less than or equal to 10."
	
.text

	li $v0, 4       #print string prompt
	la $a0, prompt
	syscall
	
	li $v0, 5       #Read 1st integer into $t0
	syscall
	move $t0, $v0
	
	li $v0, 5       #Read 2nd integer into $t1
	syscall
	move $t1, $v0
	
	li $v0, 5       #Read 3rd integer into $t2
	syscall
	move $t2, $v0
	
	add $t0, $t0, $t1    #Accumulate the sum
	add $t0, $t0, $t2
	
	bgt $t0, 10, great   #Branch if sum is greater than 10 move to label great

	li $v0, 4      # Else Print output String 2
	la $a0, less
	b exit         #Skip the next step and jump to exit
	
great: 	li $v0, 4      # Print output String if condition is true
	la $a0, greater 
exit: syscall

	li $v0, 10     # Exit the Program
	syscall

	
	
	