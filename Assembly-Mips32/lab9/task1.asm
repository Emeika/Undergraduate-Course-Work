.data
	first: .asciiz "Enter First Number: "
	second: .asciiz "Enter second number: "
	third: .asciiz "Enter third: "
	output: .asciiz "The median of the three numbers is: "

.text
	li $v0, 4
	la $a0, first
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	# ------------
	li $v0, 4
	la $a0, second
	syscall
	
	li $v0, 5
	syscall
	move $t1, $v0
	
	#--------------
	li $v0, 4
	la $a0, third
	syscall
	
	li $v0, 5
	syscall
	move $t2, $v0
	
	
	# a> b    B> c then b   if 2nd false then c is median
	
	li $v0, 4
	la $a0, output
	syscall
	
	bgt $t0, $t1, jump
	# if first is less than second then print first number
	li $v0, 1
	move $a0, $t0
	syscall
	b end
	

jump:
	bgt $t1, $t2, jump2
	# if second is less than third then print third number else jump 
	li $v0, 1
	move $a0, $t2
	syscall
	b end
jump2:
	# print second number
	li $v0, 1
	move $a0, $t1
	syscall

end: 	li $v0, 10
	syscall


	
	
	
	