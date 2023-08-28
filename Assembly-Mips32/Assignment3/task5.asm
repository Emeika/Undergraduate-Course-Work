# Convert the Question#1 into a procedure that takes array address and size of array as 
# arguments and outputs minimum, maximum and average of the array elements.

.data 
	array: .space 40 # Allocate space for array of 10 32-bit integers
	input: .asciiz "Enter a positive number: "
	size: .asciiz "Enter the size of array: "
	error: .asciiz "Error: Invalid input. Please enter a positive number: "
	newline: .asciiz "\n"
	avg: .asciiz "Average: "
	max: .asciiz "Max: "
	min: .asciiz "Min: "
	
.text
	j main	
	
calculateArray:
	li $t2, 0          # sum variable
	li $t3, 0          # max variable initialized to 0
	li $t4, 2147483647   #initialize min to the largest possible value for a 32-bit integer
	
	addi $sp, $sp, -4  # Allocate space on the stack
	sw $s0, 0($sp)     # save the original $s0 value - array adress
	
	move $s1, $s0      # move array first index address to $s1
	
	li $v0, 4  # prompt to enter input integer
	la $a0, input
	syscall
	
	li $t1, 0 # counter
loop:	
	beq $t1, $t0, print   # branch if counter == size of array
	
	li $v0, 5  # take input array element from user
	syscall
	move $s2, $v0
	
	bltz $t1 invalid   # Check if input is negative then jump to error
	add $t2, $t2, $s2  # add each element of the array
	
	sw $s2, 0($s1)
	
	bgt $s2, $t3, high  # branch if array input > than current temp variable value $t3
	blt $s2, $t4, less  # branch if array input < than current temp variable value $t4

	
	addi $t1, $t1, 1  # increment counter to run loop
	addi $s1, $s1, 4  # increment array index
	j loop 

invalid:
	li $v0, 4   # Prompt user to enter postive number
	la $a0, error
	syscall
	
	j loop  # Repeat loop

high:
	move $t3, $s2        # current array element stored in max variable
	blt $s2, $t4, less  # branch if array input < than current temp variable value $t4
	addi $s1, $s1, 4  # increment array index
	addi $t1, $t1, 1  # increment counter to run loop
	j loop

	
less: 	move $t4, $s2       # current array element stored in min variable
	addi $s1, $s1, 4  # increment array index
	addi $t1, $t1, 1  # increment counter to run loop
	j loop

print:
	div $t2, $t2, $t0  # Divide sum with number of elements to calculate average
	
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
	move $a0, $t3
	syscall
	
	#----------------- Print Min
	
	li $v0, 4
	la $a0, newline
	syscall
	
	li $v0, 4
	la $a0, min
	syscall
	
	li $v0, 1
	move $a0, $t4
	syscall
	
	lw $s0, 0($sp)
	addi $sp, $sp, 4
	jr $ra  # return 

main:	
	la $s0, array  # load address of array
	# Prompt to enter the size 
	li $v0, 4
	la $a0, size
	syscall
	
	li $v0, 5  # read size input
	syscall
	move $t0, $v0
	
	jal calculateArray
	
	li $v0, 10
	syscall 

	
	
	
	
	
	
	
	
	
	