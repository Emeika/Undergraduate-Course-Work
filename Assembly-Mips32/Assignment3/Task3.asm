.data 	
	prompt: .asciiz "Input the value for nth term: "
	x: .asciiz " x "
	equals: .asciiz " = "
	newline: .asciiz "\n"

.text 
	# Prompt the user to enter the number
	li $v0, 4
	la $a0, prompt
	syscall
	
	# Read integer into $t0
	li $v0, 5
	syscall 
	move $t0, $v0
	
	
	# Product variable
	li $s0, 1  
loop:	
	# branch if product variable > input integer
	bgt $s0, $t0, end
	mul $s1, $s0, $s0   # 1 x 1 ... product stored in $s1
	
	# Print 1*1 = 1...
	li $v0, 1   
	move $a0, $s0
	syscall
	
	li $v0, 4
	la $a0, x
	syscall
	
	li $v0, 1   
	move $a0, $s0
	syscall
	
	li $v0, 4
	la $a0, equals
	syscall	
	
	li $v0, 1   # Print product
	move $a0, $s1
	syscall
	
	li $v0, 4   #Newline
	la $a0, newline
	syscall
	
	#increment the product counter variable
	addi $s0, $s0, 1 
	
	#loop back
	j loop  
		
	
end:
	li $v0, 10
	syscall	
	
	
	
	