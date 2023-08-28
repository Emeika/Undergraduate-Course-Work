.data
	a: .word 5
	b: .word 2
	c: .word 3
	prompt: .asciiz "Enter a value for x: "
	x: .word 0
	output: .asciiz "“The result of the quadratic equation is, "
	y: .word 0
	
.text

	li $v0, 4      # Print prompt
	la $a0, prompt 
	syscall
	
	li $v0, 5    # Read Integer 
	syscall 
	sw $v0, x   # Store into variable x
	
	lw $t0, x
	lw $t1, a
	lw $t2, b
	lw $t3, c
	
	mul $s1, $t1, $t0  # mul a * x
	mul $s1, $s1, $t0  #product * x
	mul $s0, $t2, $t0  # b* x
	
	add $s1, $s1, $s0  
	add $s1, $s1, $t3
	
	sw $s1, y
	
	
	li $v0, 4    # Print output
	la $a0, output
	syscall
	
	li $v0, 1
	lw $t0, y
	move $a0, $t0
	syscall
	
	li $v0, 10
	syscall
	
	
	
	
