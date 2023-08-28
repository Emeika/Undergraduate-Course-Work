.data
	first: .asciiz "Enter a first number to calculate its factorial: "
	second: .asciiz "Enter a second number to calculate its factorial: "
	
	newline: .asciiz "\n"
	outputsecond: .asciiz "The factorial of the second number is  "
	outputfirst: .asciiz "The factorial of the first number is  "
	
	sum: .asciiz "The sum of the two factorial values is "

.text
j main
factorial:
	li $s1, 1  #product

loop:
	# branch if number($t0) is equal to 0
	beqz $t0, end
	mul $s1, $s1, $t0  # Multiply the product with the all the numbers before the input intger 3*2*1
	subi $t0, $t0, 1   #decrement number counter by 1 for each loop
	j loop
end:	
	
	jr $ra
	
main:
	li $s3, 0  #Sum variable
	
	# Prompt to enter the 1st number
 	li $v0, 4
	la $a0, first
	syscall
	
	# read 1st integer into $t0
	li $v0, 5 
	syscall
	move $t0, $v0
	
	# Function call 
	# pc stores the first instruction address of the function
	# ra stores the next instruction after function call
	jal factorial 

 	# Print output factorial number
   	li $v0, 4
	la $a0, outputfirst
	syscall
	
	# The calculated factorial is stored in $s1 in the function
	li $v0, 1
	move $a0, $s1
	syscall
	
	add $s3, $s3, $s1  # add first factorial answer into $s3
		
	# ---------------------------------------
	# Prompt to enter the 2nd number
	li $v0, 4
	la $a0, second
	syscall
	
	# read 2nd integer into $t0
	li $v0, 5
	syscall
	move $t0, $v0
	
	# Function call 
	jal factorial
	
	li $v0, 4  # New line
	la $a0, second
	syscall
	
	# Print output factorial number
	li $v0, 4
	la $a0, outputsecond
	syscall
	
	li $v0, 1
	move $a0, $s1
	syscall
	
	add $s3, $s3, $s1  # add second factorial answer into $s3  (1st fact + 2nd fact)
	
	
	#---------
	li $v0, 4  # New line
	la $a0, second
	syscall
	
	# Print Sum output 
	li $v0, 4
	la $a0, sum
	syscall
	
	li $v0, 1
	move $a0, $s3
	syscall
	
	# end 
	li $v0, 10 
	syscall
	
	
	

	
