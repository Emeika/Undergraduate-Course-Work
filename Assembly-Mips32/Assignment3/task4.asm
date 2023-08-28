.data 	
	input: .asciiz "Input number of terms: "
	output: .asciiz "The odd numbers are: "
	oddsum: .asciiz "The Sum of odd Natural Numbers upto 5 terms: "

.text
	# Prompt user to enter the number
	li $v0, 4  
	la $a0, input
	syscall
	
	# Read integer into $t0
	li $v0, 5
	syscall 
	move $t0, $v0
	
	# Print output odd numbers 
	li $v0, 4  
	la $a0, output
	syscall
	
	li $s0, 0  # Counter 
	li $s1, 1  # odd number variable
	li $s2, 0  # sum variable
	
loop:  
	beq $s0, $t0, sum  # if counter == input intger then branch outside loop
	
	# print odd number
	li $v0, 1
	move $a0, $s1
	syscall
	
	# add the odd numbers
	add $s2, $s2, $s1  
	
	addi $s1, $s1, 2    # add to get the next odd number stored in $s1 (1+2 = 3)
	
	li $v0, 11          # System call code for printing a character
        li $a0, 32          # ASCII value of the space character
        syscall             # Print the space character
	
	addi $s0, $s0, 1  #Increment the counter 
	j loop  	  # loop runs

sum:	
	li $v0, 11          # System call code for printing a character
        li $a0, 10          # ASCII value of the newline character
        syscall             # Print the newline character

	# Print output message for sum of odd numbers
	li $v0, 4
	la $a0, oddsum
	syscall
	
	li $v0, 1
	move $a0, $s2
	syscall


	li $v0, 10
	syscall
	
	
	
	
	
		