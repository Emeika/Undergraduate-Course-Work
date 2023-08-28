.data 
	arr: .word 1,2,3,4,5,6,7,8,9,10
	num1: .asciiz "Number 1: "
	num2: .asciiz "Number 2: "
	var3: .word 0
	result: .asciiz "Result of div: "
	
.text	
	# Task1
	li $t1, 5
	li, $t2, 10
	
	move $t3, $t1  # move t1 to t3
	
	# Move t2 to t1
	move $t1, $t2
	move $t2, $t3
	
	# Task 2
	
	la $s0, arr  # Load arr
	
	lw $s1, 20($s0)  # Load the value of 6th position to $s1
	lw $s2, 36($s0)  # Load the value of 10th position to $s2
	
	add $s3, $s1,$s2  # add 6th and 10th value and store to $s3
	
	sw $s3, 28($s0)   # override and storte the value of addition($s3) to the 8thpositoin 
	# store $s3 to s0
	
	
	
	# Task 3
	
	# Prompt
	
	li $v0, 4
	la $a0, num1
	syscall
	
	# get 
	li $v0, 5
	syscall
	
	# store into $t0
	move $t0, $v0
	
	
	# for the second number
	li $v0, 4
	la $a0, num2
	syscall
	# get 
	li $v0, 5
	syscall
	# store into $t1
	move $t1, $v0
	
	
	# add
	
	add $t3, $t0, $t1
	
	
	li $s0, 2
	div $t2, $t3, $s0  # divide by 2
	sw $t2, var3  #store to var3
	
	li $v0, 4
	la $a0, result
	syscall
	li $v0, 1
	lw $s1, var3
	move $a0, $s1 #move s1 to a0
	syscall
	
	li $v0, 10
	syscall	
	
	
	
	
	
	
	
	