.data
	prompt: .asciiz "Enter an integer: "
	output: .asciiz "The number "
	is: .asciiz " is "
	odd: .asciiz " odd"
	even: .asciiz " even"

.text
	la $a0, prompt
	li $v0, 4
	syscall
	
	li, $v0, 5
	syscall
	move $t0, $v0
	
	andi $t1, $t0, 1  # And with 1 to get the least vsignificant bit 
	srl $t1, $t1, 0  # shift right by 0 to get the least significant bit
	beq $t1, 0, evenloop
oddloop:
	li, $v0, 4
	la $a0, output
	syscall
	
	li $v0, 1
	move $a0, $t0
	syscall
	
	li, $v0, 4
	la $a0, is
	syscall
	
	li, $v0, 4
	la $a0, odd
	syscall
	j end

	
evenloop:
	li, $v0, 4
	la $a0, output
	syscall
	
	li $v0, 1
	move $a0, $t0
	syscall
	
	li, $v0, 4
	la $a0, is
	syscall
	
	li, $v0, 4
	la $a0, even
	syscall
	
	j end

	
end: 
	li $v0, 10
	syscall
