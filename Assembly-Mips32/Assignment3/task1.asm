# Q1Write a MIPS assembly program that takes ten input of positive numbers only, place them in 
# an array. Find the minimum number, maximum number and average. Prompt the user 
# properly and also ask for the number again if user enters a negative number or a character 
.data 
	array: .space 40 # Allocate space for array of 10 32-bit integers
	prompt: .asciiz "Enter a positive number: "
	error: .asciiz "Error: Invalid input. Please enter a positive number: "
	newline: .asciiz "\n"
	avg: .asciiz "Average: "
	max: .asciiz "Max: "
	min: .asciiz "Min: "
	

.text
	la $s0, array  # Load Address of array
	li $t0, 0    # Index
	
	
	li $v0, 4    #Prompt user to enter number
	la $a0, prompt
	syscall
	
loop:
	beq $t0, 10, continue  # Branch if $t0(Index) is equal to 10 then array is complete
	
	li $v0, 5    #Get input Intger for array into t1
	syscall 
	move $t1, $v0
	
	bltz $t1 invalid  #Check if input is negative then jump to error
	
	
	sw $t1, 0($s0)  # Store input in array
	addi $s0, $s0, 4  # Increment array address
	addi $t0, $t0, 1  # Increment index variable
	
	j loop  # Repeat loop
	
invalid:
	li $v0, 4   # Prompt user to enter postive number
	la $a0, error
	syscall
	
	j loop  # Repeat loop

continue:

	li $t2, 0 # Sum
	li $t1, 10 # Counter 
	
	addi $s0, $s0, -4  # last index element of array
	 
	lw $s1, 0($s0)  #Load array last element into $t3
	
	move $t4, $s1  #initialize max to the last elemeent
	move $t5, $s1
	#li $t5, 2147483647   #initialize min to the largest possible value for a 32-bit integer
	
loop2:
	beqz $t1, end   # if counter == 0 then jump to end
	lw $s1, 0($s0)  #Load array last element into $ts1
	add $t2, $t2, $s1  # Add each element of array to sum $t2
	bgt $s1, $t4, high  # branch if array element > than current temp variable value $t4
	blt $s1, $t5, less  # j less
	
	addi $s0, $s0, -4    # decrement index to the previous element 
	addi $t1, $t1, -1    # Decrement the counter 
	j loop2
	
high:
	move $t4, $s1        # current array element stored in max variable
	addi $s0, $s0, -4    # decrement index to the previous element 
	addi $t1, $t1, -1    # Decrement the counter
	j loop2

	
less: 	move $t5, $s1       # current array element stored in min variable
	addi $s0, $s0, -4   # decrement index to the previous element 
	addi $t1, $t1, -1   # Decrement the counter 
	j loop2

end:
	div $t2, $t2, 10  # Divide sum with 10 to calculate average
	
	#----------------- Print Average
	li $v0, 4
	la $a0, newline
	syscall
	
	li $v0, 4
	la $a0, avg
	syscall
	
	li $v0, 1
	move $a0, $t2
	syscall
	#----------------- Print Max
	
	li $v0, 4
	la $a0, newline
	syscall
	
	li $v0, 4
	la $a0, max
	syscall
	
	li $v0, 1
	move $a0, $t4
	syscall
	
	#----------------- Print Min
	
	li $v0, 4
	la $a0, newline
	syscall
	
	li $v0, 4
	la $a0, min
	syscall
	
	li $v0, 1
	move $a0, $t5
	syscall
	
	
	
	li $v0, 10
	syscall 
