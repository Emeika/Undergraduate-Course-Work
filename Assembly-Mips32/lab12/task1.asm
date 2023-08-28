.data
	prompt: .asciiz "Enter an integer: "
	true_result: .asciiz "Number is a prime number"
	false_result: .asciiz "Number is not a prime number"
	
.text
	# take input
	li $v0, 4
	la $a0, prompt
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	# div num from 2 till n-1
	# t1 = divisor
	li $t1, 2
	la $s1, ($t0)
	subi $s1, $s1, 1 # n-1
	loop:
		div $t2, $t0, $t1
		mfhi $s0 # get remainder
		
		addi $t1, $t1, 1 # inc counter
		beq $t1, $s1, not_prime
		beqz $s0, loop
		j prime
		
	not_prime:
		li $v0, 4
		la $a0, false_result
		syscall
		j end
				
	prime:
		li $v0, 4
		la $a0, true_result
		syscall
		
	end:
		li $v0, 10
		syscall
		