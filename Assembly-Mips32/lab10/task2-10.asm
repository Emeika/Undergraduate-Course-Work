.data 
	start_index: .asciiz "Enter the first integer in the series: " 
	int_num: .asciiz "Enter number of integers in the series: "
	step_size: .asciiz "Enter step value: "
	series: .asciiz "The series is: "
	sum: .asciiz "The summation is: "
	avg: .asciiz "The average is: "
	choice: .asciiz "Do you like to take another try [y/n]? "
	comma: .asciiz " , "
	newline: .asciiz "\n"

.text 

main: 
	# prompt user to enter the first num in the series into $s0
	li $v0, 4
	la $a0, start_index
	syscall
	
	li $v0, 5
	syscall
	move $s0, $v0

	# Prompt user to enter number of intgers into $s1
	li $v0, 4
	la $a0, int_num
	syscall
	
	li $v0, 5
	syscall
	move $s1, $v0		
	
	# Prompt user to enter step value size into $s2
	li $v0, 4
	la $a0, step_size
	syscall
	
	li $v0, 5
	syscall
	move $s2, $v0	
	
	# print output
	li $v0, 4
	la $a0, series
	syscall
	
	jal print_series # pc is the first instructuion of the function and ra is the next instruction
	b end
	
print_series:
	#adjust stack to store the parameters 
	addi $sp, $sp, -12
	sw $s0, 0($sp)  # first series number
	sw $s1, 4($sp)  # number of int
	sw $s2, 8($sp)	# step size
	
	move $t0, $s0 # sum variable
	
	li $v0, 1  # print first number 
	move $a0, $s0
	syscall 
	addi $s1, $s1, -1
	

loop:	beqz $s1, return 
	
	#print comma
	li $v0, 4
	la $a0, comma
	syscall
	
	# step up 
	add $s0, $s0, $s2
	
	li $v0, 1  # print number
	move $a0, $s0
	syscall 
	
	# decrement the loop counter
	addi $s1, $s1, -1
	
	add $t0, $t0, $s0  #sum the numbers
	j loop
return:
	
	li $v0, 4
	la $a0, newline
	syscall
	
	# print sum
	li $v0, 4
	la $a0, sum
	syscall
	
	li $v0, 1
	move $a0, $t0
	syscall 
	

	# restore the values which makes the paramters unchanged
	lw $s0, 0($sp)
	lw $s1, 4($sp)
	lw $s2, 8($sp)
	addi $sp, $sp, 12
	
	li $v0, 4
	la $a0, newline
	syscall
	
	# calculate average 
	div $t0, $t0, $s1
	# print average
	li $v0, 4
	la $a0, avg
	syscall
	
	li $v0, 1
	move $a0, $t0
	syscall 

	li $v0, 4
	la $a0, newline
	syscall
	
	# prompt user to try take another try
	li $v0, 4
	la $a0, choice
	syscall
	
	li $v0, 12  #read choice character
	syscall
	move $t1, $v0
	
	li $v0, 4
	la $a0, newline
	syscall
	
	beq $t1, 'y', main
	
	jr $ra  # jump register unconditionally to ra
	
	
end:
	li $v0, 10
	syscall
	
	
	
	
	
	
